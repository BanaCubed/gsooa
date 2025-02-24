import { ref, type Ref } from 'vue';

const activeQuestionTypes = ref<boolean[]>([]);
for (let i = 0; i < 1 /* `TODO` *Find some way to automate this* */; i++) {
    activeQuestionTypes.value[i] = true;
}

/**
 * @returns Array of indexes representing the active question types.
 */
export function getActiveQuestionTypes(): number[] {
    const types: number[] = [];
    for (let i = 0; i < activeQuestionTypes.value.length; i++) {
        const questionType = activeQuestionTypes.value[i];
        if (questionType === true) {
            types.push(i);
        }
    }
    return types;
}

// console.log(activeQuestionTypes.value);

interface Config {
    /**
     * An ref to an array containing booleans representing whether each question type is enabled.
     */
    activeQuestionTypes: Ref<boolean[]>;
}

const config: Config = {
    activeQuestionTypes,
};

export default config;
