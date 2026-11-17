// How large the emulator draws the game: a multiple of its native resolution,
// or a letterboxed fit inside a window.

/** A size in CSS pixels. */
export interface CanvasSize {
  width: number;
  height: number;
}

/**
 * The size to draw the game canvas at.
 *
 * A number is that multiple of the native resolution, whatever the box. `auto`
 * leaves EmulatorJS' fill-the-box stretch alone, except in a window, where the
 * game is letterboxed so the window keeps the game's shape.
 *
 * Returns null when EmulatorJS' own 100%x100% is the right answer.
 */
export function canvasDisplaySize(
  native: CanvasSize,
  scale: number | "auto",
  box: CanvasSize,
  windowed: boolean,
): CanvasSize | null {
  if (scale !== "auto") {
    return { width: native.width * scale, height: native.height * scale };
  }
  if (!windowed || box.width <= 0 || box.height <= 0) return null;
  const fit = Math.min(box.width / native.width, box.height / native.height);
  return {
    width: Math.max(1, Math.floor(native.width * fit)),
    height: Math.max(1, Math.floor(native.height * fit)),
  };
}
