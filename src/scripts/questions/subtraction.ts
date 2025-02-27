import { prng } from '../prng';
import { QuestionTypes, type QuestionData, type QuestionProperties } from './_questions';

export const properties: QuestionProperties = {
    minLevel: 2,
    maxLevel: 12,
    limits: (lvl, i) => [(1.35 ** lvl * lvl + 3) / 2 ** i, (1.35 ** lvl * lvl + 7) / 2 ** (i - 1)],
    inputs: 1,
    outputs: () => 2,
};

class Addition {
    type = QuestionTypes.Subtraction;
    variables: number[] = [];
    answer: number[] = [];
    #properties = properties; // This is seperate from the static property to allow for usage of the `this` keyword

    constructor(lvl: number, seed: number) {
        // --- Error Throwing ---
        if (lvl < this.#properties.minLevel) {
            throw new Error(
                `Question of type "Subtraction" has a minimum level of "${this.#properties.minLevel}", whereas the current level is "${lvl}"`,
            );
        }
        if (lvl > (this.#properties.maxLevel ?? 0) && this.#properties.maxLevel !== undefined) {
            throw new Error(
                `Question of type "Subtraction" has a maximum level of "${this.#properties.minLevel}", whereas the current level is "${lvl}"`,
            );
        }
        // --- Output Generation ---
        for (let i = 0; i < this.#properties.outputs(lvl); i++) {
            let num = prng(seed + i);
            const limits = this.#properties.limits(lvl, i);
            const range = limits[1] - limits[0];
            num = Math.round(num * range);
            this.variables.push(num);
        }
        // --- Answer Calculation ---
        let answer = this.variables[0];
        for (let i = 1; i < this.variables.length; i++) {
            answer -= this.variables[i];
        }
        this.answer.push(answer);
    }

    static properties: QuestionProperties = properties;
}

export interface AdditionQuestionData extends QuestionData {
    type: QuestionTypes.Subtraction;
    answer: [number];
}

export default Addition;
