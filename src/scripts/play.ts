import { ref, type Ref } from 'vue';
import type { Question } from './questions/questions';

export interface PlayData {
    seed: number;
    level: number;
    health: number;
    difficulty: number;
    /**
     * Tracks the amount of questions answered correctly.
     * Certain types of questions may give more score than others.
     * Final score at the end of a play is calculated non-linearly based off this score.
     */
    score: number;
    active: boolean;
    currentQuestion: Question;
}

const playData: Ref<PlayData> = ref({
    seed: 0,
    level: 0,
    health: 0,
    difficulty: 0,
    score: 0,
    active: false,
    currentQuestion: {
        type: 0,
        variables: [],
        answer: [],
    },
});

export default playData;

export function startPlay(seed: number): void {
    playData.value.seed = seed;
}
