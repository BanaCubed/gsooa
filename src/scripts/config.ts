import { ref, type Ref } from "vue";

export enum QuestionTypes {
    Addition,
    Subtraction,
    Multiplication,
    Division,
    Exponentiation,
    length // Exists for automating the incrementing of the below for loop
}

const activeQuestionTypes = ref<boolean[]>([]);
for (let i = 0; i < QuestionTypes.length; i++) {
    activeQuestionTypes.value[i] = true;
}

console.log(activeQuestionTypes.value);

interface Config {
    /**
     * An ref to an array containing booleans representing whether each question type is enabled.
     */
    activeQuestionTypes: Ref<boolean[]>;
}

const config: Config = {
    activeQuestionTypes
}

export default config;
