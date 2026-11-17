// usePlayerDisplayPref: shared "how the game is drawn" preferences.
// Keyed on `emulation.*` so a choice made in one player is the one the next
// player opens with.
import type { RemovableRef } from "@vueuse/core";
import { useUserLocalStorage } from "@/composables/useUserLocalStorage";

/** A multiple of the game's native resolution, or `"auto"` to fill the stage. */
export type PlayerScale = number | "auto";

const windowed = useUserLocalStorage<boolean>("emulation.windowed", false);
const scale = useUserLocalStorage<PlayerScale>("emulation.scale", "auto");

export function usePlayerDisplayPref(): {
  windowed: RemovableRef<boolean>;
  scale: RemovableRef<PlayerScale>;
} {
  return { windowed, scale };
}
