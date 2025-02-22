import { QuestionTypes, type Question, type QuestionProperties } from './questions';

const properties: QuestionProperties = {
    minLevel: 0,
    limits: (lvl) => [1.25 ** lvl * lvl, 1.35 ** lvl * lvl + 7],
    inputs: 1,
    outputs: () => 2,
};

const Addition = {
    id: QuestionTypes.Addition,
    properties,
};

export interface QuestionAddition extends Question {
    type: QuestionTypes.Addition;
    answer: [number];
}

export default Addition;
