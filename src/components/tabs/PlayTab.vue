<template>
    <Transition>
        <button v-on:click="playData.active = true" v-if="!playData.active" class="playButton">
            <span class="material-symbols-rounded">play_circle</span>Play
        </button>
        <QuestionContainer v-else-if="playData.active" :key="playData.score" />
    </Transition>
</template>

<script setup lang="ts">
import playData from '@/scripts/play';
import QuestionContainer from '../questions/QuestionContainer.vue';
</script>

<style lang="css" scoped>
.v-leave-to {
    translate: calc(-50% - 100px) 0;
    opacity: 0;
}

.v-enter-from {
    translate: calc(-50% + 100px) 0;
    opacity: 0;
}

.v-enter-to,
.v-leave-from {
    translate: calc(-50%) 0;
    opacity: 1;
}

.v-enter-active,
.v-leave-active {
    transition: 1s ease-in-out;
}

.playButton:not(.v-enter-active):not(.v-leave-active) {
    translate: -50% 0;
}

.playButton {
    position: absolute;
    left: 50%;
}
</style>
