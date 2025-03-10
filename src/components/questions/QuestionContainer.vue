<template>
    <div id="questionContainer">
        <h3>
            Level {{ playData.level }}<br /><span
                class="material-symbols-rounded"
                :class="{ empty: playData.health <= i }"
                v-for="(hp, i) in new Array(5)"
                >favorite</span
            ><br /><LevelBar />
        </h3>
        <br />
        <div id="question">
            <component :is="questionComponents[playData.currentQuestion.type]" /><br />
            <div ref="inputs" id="inputs">
                <input
                    type="number"
                    v-for="(answer, i) in playData.currentQuestion.answer"
                    placeholder="0"
                    name="John"
                    :id="i === 0 ? 'firstInput' : ''"
                />
            </div>
        </div>
        <button v-on:click="answer()">
            <span class="material-symbols-rounded">edit</span>Answer
        </button>
    </div>
</template>

<script setup lang="tsx">
import playData from '@/scripts/play';
import AdditionQuestion from './AdditionQuestion.vue';
import SubtractionQuestion from './SubtractionQuestion.vue';
import type { JSX } from 'vue/jsx-runtime';
import { useTemplateRef, watch } from 'vue';
import questions from '@/scripts/questions/_questions';
import LevelBar from '../LevelBar.vue';

document.addEventListener('keydown', (ev) => {
    if (ev.key === 'Enter') {
        answer();
    }
});

const questionComponents: JSX.Element[] = [<AdditionQuestion />, <SubtractionQuestion />];

const inputRefs = useTemplateRef('inputs');

// This has to be _here_, because it references inputRefs.
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
        element.value = '';
    }
    if (!correct) {
        playData.value.health--;
        if (playData.value.health <= 0) {
            playData.value.active = false;
        }
    }
    if (correct) {
        playData.value.score++;
        if (playData.value.score >= 1.1 ** playData.value.level * 5 * playData.value.level) {
            playData.value.level++;
        }
    }
    playData.value.seed++;
    playData.value.currentQuestion = questions.generate(playData.value.level, playData.value.seed);
}

defineExpose({
    answer,
});
</script>

<style lang="css" scoped>
#question {
    margin: auto;
    margin-bottom: 20px;
    background-color: var(--color-background-soft);
    padding: 5px 5px;
    border-radius: 4px;
    min-width: 160px;
    width: fit-content;
}

#questionContainer:not(.v-enter-active):not(.v-leave-active) {
    translate: -50% 0;
}

#questionContainer {
    position: absolute;
    left: 50%;
}

.empty {
    font-variation-settings: 'FILL' 0;
    transition: 0.5s all cubic-bezier(0.075, 0.82, 0.165, 1);
}
</style>

<style lang="css">
input {
    width: 100%;
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
