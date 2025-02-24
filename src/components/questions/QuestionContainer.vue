<template>
    <div id="questionContainer">
        Level {{ playData.level }} | {{ playData.score }} Points<br>
        <component :is="questionComponents[playData.currentQuestion.type]" />
    </div>
</template>

<script setup lang="tsx">
import playData from '@/scripts/play';
import AdditionQuestion from './AdditionQuestion.vue';
import type { JSX } from 'vue/jsx-runtime';

const questionComponents: JSX.Element[] = [
    <AdditionQuestion />
]

// comment
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
