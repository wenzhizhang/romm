import { describe, expect, it } from "vitest";
import { canvasDisplaySize } from "./playerDisplay";

const GBA = { width: 240, height: 160 };
const VIEWPORT = { width: 1920, height: 1080 };

describe("canvasDisplaySize", () => {
  it("draws a multiple of the native resolution", () => {
    expect(canvasDisplaySize(GBA, 1, VIEWPORT, false)).toEqual({
      width: 240,
      height: 160,
    });
    expect(canvasDisplaySize(GBA, 3, VIEWPORT, true)).toEqual({
      width: 720,
      height: 480,
    });
    expect(canvasDisplaySize(GBA, 8, VIEWPORT, false)).toEqual({
      width: 1920,
      height: 1280,
    });
  });

  it("leaves the fill behaviour alone when auto outside a window", () => {
    expect(canvasDisplaySize(GBA, "auto", VIEWPORT, false)).toBeNull();
  });

  it("letterboxes auto into a window", () => {
    expect(
      canvasDisplaySize(GBA, "auto", { width: 800, height: 800 }, true),
    ).toEqual({ width: 800, height: 533 });
  });

  it("waits for a measured box", () => {
    expect(
      canvasDisplaySize(GBA, "auto", { width: 0, height: 0 }, true),
    ).toBeNull();
  });

  it("never rounds a fit down to nothing", () => {
    expect(
      canvasDisplaySize(GBA, "auto", { width: 10, height: 10 }, true),
    ).toEqual({ width: 10, height: 6 });
  });
});
