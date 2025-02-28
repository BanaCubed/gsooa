import { ref, type Ref } from 'vue';
import type { QuestionData } from './questions/_questions';
import questions from './questions/_questions';

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
    currentQuestion: QuestionData;
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

export function startPlay(seed?: number): void {
    seed = seed ?? Math.random(); // The general size of the seed variable is irrelevant.
    playData.value.seed = seed;
    playData.value.active = true;
    playData.value.score = 0;
    playData.value.level = 1;
    playData.value.health = 5;
    playData.value.difficulty = 1;
    playData.value.currentQuestion = questions.generate(1, seed);
}
