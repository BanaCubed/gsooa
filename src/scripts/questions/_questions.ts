import { getActiveQuestionTypes } from '../config';
import { prng } from '../prng';
import Addition, { properties as additionProperties } from './addition';
import Subtraction, { properties as subtractionProperties } from "./subtraction";

/**
 * Generic interface matching any question stored in the `playData` object.
 */
export interface QuestionData {
    type: QuestionTypes;
    variables: number[];
    answer: number[];
}

export enum QuestionTypes {
    Addition,
    Subtraction,
    Multiplication,
    Division,
    Exponentiation,
}

interface QuestionTypeData {
    name: string;
    properties: QuestionProperties;
}
/**
 * Utility array containing the properties of quesiton types. Used in other functions in this file.
 */
const questionTypesData: QuestionTypeData[] = [
    {
        name: 'Addition',
        properties: additionProperties,
    },
    {
        name: 'Subtraction',
        properties: subtractionProperties,
    },
];

/**
 * The properties of a question type. This is not a generic type, and thus should not be extended.
 *
 * Custom properties are allowed, but can only be used in the creation function.
 */
export interface QuestionProperties {
    /**
     * The lowest level within a play that the question type can appear.
     *
     * `TODO` *Make it so that your highest level is saved, and you can only disable question types after encountering them.*
     */
    minLevel: number;
    /**
     * The highest level the question type can appear in. Intended for swapping out appearences and formulae.
     */
    maxLevel?: number;
    /**
     * Function calculating the lower and upper bounds that a given value in the question formula can be.
     * @param lvl The current level of the play.
     * @param i The index of the vale to calculate.
     * @returns Minimum and maximum values for a given value in the formula at a given level.
     */
    limits: (lvl: number, i: number) => [number, number];
    /**
     * The amount of inputs the player needs to enter.
     *
     * `TODO` *Allow for changing the naming scheme of these easily.*
     */
    inputs: number;
    /**
     * The amount of values generated. Can be a function.
     *
     * **FUNCTION SHOULD NOT HAVE RANDOMNESS BECAUSE OF SEEDS**
     *
     * `TODO` *Allow for usage of seeds in output count.*
     */
    outputs: (lvl: number) => number;
}

function questionsAvailableAtLevel(lvl: number): number[] {
    const questions = getActiveQuestionTypes();
    for (let i = 0; i < questions.length; i++) {
        const properties = questionTypesData[i].properties;
        properties.maxLevel ??= Infinity;
        if (lvl < properties.minLevel || lvl > properties.maxLevel) {
            questions.splice(i);
        }
    }
    if (questions.length === 0) {
        console.warn(`All possible questions are invalid at level ${lvl}. Ignoring config`);
    }
    return questions;
}

const questionClasses = [Addition, Subtraction];

function generateQuestion(lvl: number, seed: number): QuestionData {
    const types = questionsAvailableAtLevel(lvl);
    console.log(types);
    let i = Math.floor(prng(seed) * types.length);
    i = types[i];
    return new questionClasses[i](lvl, seed);
}

const questions = {
    generate: generateQuestion, // These have different names to remove redundancy
    availableAtlevel: questionsAvailableAtLevel,
};

export default questions;
