import { prng } from '../prng';
import { QuestionTypes, type QuestionData, type QuestionProperties } from './questions';

const properties: QuestionProperties = {
    minLevel: 1,
    maxLevel: 10,
    limits: (lvl) => [1.25 ** lvl * lvl, 1.35 ** lvl * lvl + 7],
    inputs: 1,
    outputs: () => 2,
};

class Addition {
    type = QuestionTypes.Addition;
    variables: number[] = [];
    answer: number[] = [];
    #properties = properties; // This is seperate from the static property to allow for usage of `this`

    constructor(lvl: number, seed: number) {
        // --- Error Throwing ---
        if (lvl < this.#properties.minLevel) {
            throw new Error(
                `Question of type "Addition" has a minimum level of "${this.#properties.minLevel}", whereas the current level is "${lvl}"`,
            );
        }
        if (lvl > (this.#properties.maxLevel ?? 0) && this.#properties.maxLevel !== undefined) {
            throw new Error(
                `Question of type "Addition" has a maximum level of "${this.#properties.minLevel}", whereas the current level is "${lvl}"`,
            );
        }
        // --- Output Generation ---
        for (let i = 0; i < this.#properties.outputs(lvl); i++) {
            let num = prng(seed + i);
            const limits = this.#properties.limits(lvl, i);
            const range = limits[1] - limits[0];
            num = Math.floor(num * range);
            this.variables.push(num);
        }
        // --- Answer Calculation ---
        let answer = 0;
        for (let i = 0; i < this.variables.length; i++) {
            answer += this.variables[i];
        }
        this.answer.push(answer);
    }

    static properties: QuestionProperties = properties;
}

export interface AdditionQuestionData extends QuestionData {
    type: QuestionTypes.Addition;
    answer: [number];
}

export default Addition;
