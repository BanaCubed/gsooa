import { ref } from "vue";

const playData = ref({
    seed: 0,
    level: 0,
    health: 0,
    difficulty: 0
});

export default playData;

export function startPlay(seed: number): void {
    playData.value.seed = seed;
}
