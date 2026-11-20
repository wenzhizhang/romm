import { describe, expect, it } from "vitest";
import { galleryRowHeight } from "./index";

// Cover box height = round(cardWidth / ratio); chrome (label + gaps +
// bottom padding) = 51px added on top.
describe("galleryRowHeight", () => {
  it("defaults to the md box-art card (158 / (2/3) + 51 = 288)", () => {
    expect(galleryRowHeight()).toBe(288);
  });

  it("shrinks for the 3D box ratio (158 / 0.75 + 51 = 262)", () => {
    expect(galleryRowHeight(3 / 4)).toBe(262);
  });

  it("is shortest for square physical / miximage art (158 + 51 = 209)", () => {
    expect(galleryRowHeight(1)).toBe(209);
  });

  it("scales with a narrower card width (phones: 108 / (2/3) + 51 = 213)", () => {
    expect(galleryRowHeight(2 / 3, 108)).toBe(213);
  });
});
