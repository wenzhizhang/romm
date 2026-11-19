import { mount } from "@vue/test-utils";
import { describe, expect, it, vi } from "vitest";
import type { UpdateRom } from "@/services/api/rom";
import { romFixture } from "@/utils/rom.fixtures";
import AdditionalDetails from "./AdditionalDetails.vue";

vi.mock("vue-i18n");

const RComboboxField = {
  props: {
    label: { type: String, default: "" },
    allowCommas: { type: Boolean, default: false },
    items: { type: Array, default: () => [] },
  },
  emits: ["update:modelValue"],
  template: `<div />`,
};

function titlesField(wrapper: ReturnType<typeof mountDetails>) {
  const field = wrapper
    .findAllComponents(RComboboxField)
    .find((c) => c.props("label") === "rom.alternative-titles");
  if (!field) throw new Error("Alternative titles field not rendered");
  return field;
}

function mountDetails(rom: UpdateRom) {
  return mount(AdditionalDetails, {
    props: { rom },
    global: {
      stubs: { RComboboxField, RDateField: true, RTextField: true },
    },
  });
}

function fieldByLabel(wrapper: ReturnType<typeof mountDetails>, label: string) {
  const field = wrapper
    .findAllComponents(RComboboxField)
    .find((c) => c.props("label") === label);
  if (!field) throw new Error(`${label} field not rendered`);
  return field;
}

describe("AdditionalDetails alternative titles", () => {
  it("writes the titles into the manual metadata", async () => {
    const rom = romFixture({ manual_metadata: { genres: ["Racing"] } });
    const wrapper = mountDetails(rom);

    await titlesField(wrapper).vm.$emit("update:modelValue", ["ACNH"]);

    expect(wrapper.emitted("update:rom")?.[0]?.[0]).toMatchObject({
      manual_metadata: { genres: ["Racing"], alternative_names: ["ACNH"] },
    });
  });

  it("keeps the commas inside a title", () => {
    const wrapper = mountDetails(romFixture({}));

    expect(titlesField(wrapper).props("allowCommas")).toBe(true);
  });

  it("clears the titles", async () => {
    const rom = romFixture({
      manual_metadata: { alternative_names: ["ACNH"] },
    });
    const wrapper = mountDetails(rom);

    await titlesField(wrapper).vm.$emit("update:modelValue", []);

    expect(wrapper.emitted("update:rom")?.[0]?.[0]).toMatchObject({
      manual_metadata: { alternative_names: [] },
    });
  });
});

describe("AdditionalDetails languages and regions", () => {
  it("writes a language onto the rom, not the manual metadata", async () => {
    const wrapper = mountDetails(romFixture({ languages: ["English"] }));

    await fieldByLabel(wrapper, "rom.languages").vm.$emit("update:modelValue", [
      "Chinese",
    ]);

    expect(wrapper.emitted("update:rom")?.[0]?.[0]).toMatchObject({
      languages: ["Chinese"],
    });
  });

  it("writes a region onto the rom", async () => {
    const wrapper = mountDetails(romFixture({ regions: ["USA"] }));

    await fieldByLabel(wrapper, "rom.regions").vm.$emit("update:modelValue", [
      "China",
    ]);

    expect(wrapper.emitted("update:rom")?.[0]?.[0]).toMatchObject({
      regions: ["China"],
    });
  });

  it("offers the canonical names as suggestions", () => {
    const wrapper = mountDetails(romFixture({}));

    expect(fieldByLabel(wrapper, "rom.languages").props("items")).toContain(
      "Chinese",
    );
    expect(fieldByLabel(wrapper, "rom.regions").props("items")).toContain(
      "China",
    );
  });
});
