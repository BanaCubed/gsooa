<template>
    <div id="questionContainer">
        Level {{ playData.level }} | {{ playData.score }} Points | {{ playData.health }}<br />
        <component :is="questionComponents[playData.currentQuestion.type]" /><br />
        <div ref="inputs">
            <input
                type="number"
                v-for="answer in playData.currentQuestion.answer"
                :key="answer.toString() + playData.seed"
            />
        </div>
        <button v-on:click="answer()">submit</button>
    </div>
</template>

<script setup lang="tsx">
import playData from '@/scripts/play';
import AdditionQuestion from './AdditionQuestion.vue';
import type { JSX } from 'vue/jsx-runtime';
import { useTemplateRef } from 'vue';
import questions from '@/scripts/questions/questions';

const questionComponents: JSX.Element[] = [<AdditionQuestion />];

const inputRefs = useTemplateRef('inputs');

function answer() {
    // @ts-expect-error TS doesn't recognise that the only possible values for inputs to contain are input elements, so the extra type annotation is required to allow `element.value` to work.
    const inputs: HTMLInputElement[] = Array.from(inputRefs.value?.childNodes ?? []);
    // console.log(inputs);
    inputs.shift();
    inputs.pop(); // These are required to get rid of the parent div.
    let correct: boolean = true;
    for (let i = 0; i < inputs.length; i++) {
        const element = inputs[i];
        try {
            if (
                Number.parseInt(element.value) !== playData.value.currentQuestion.answer[i] &&
                Number.parseFloat(element.value) !== playData.value.currentQuestion.answer[i]
            ) {
                correct = false;
                // console.log(element.value);
                // console.log(playData.value.currentQuestion.answer[i]);
            }
        } catch {
            // Better safe than sorry
            return;
        }
    }
    if (!correct) {
        playData.value.health--;
    }
    if (correct) {
        playData.value.score++;
    }
    playData.value.seed++;
    playData.value.currentQuestion = questions.generate(playData.value.level, playData.value.seed);
}

defineExpose({
    answer,
});
</script>

<style lang="css" scoped>
#questionContainer:not(.v-enter-active):not(.v-leave-active) {
    translate: -50% 0;
}

#questionContainer {
    position: absolute;
    left: 50%;
}
</style>

<style lang="css">
input {
    width: 100px;
    background-color: var(--color-background-mute);
    border: 2px solid var(--color-border);
    border-radius: 4px;
    color: var(--color-text);
}

input[type='number']::-webkit-inner-spin-button,
input[type='number']::-webkit-outer-spin-button {
    opacity: 0;
    display: none;
}
</style>
