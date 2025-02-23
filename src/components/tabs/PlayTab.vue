<template>
    <Transition>
        <button v-on:click="playData.active = true" v-if="!playData.active" class="playButton">
            <span class="material-symbols-rounded">play_circle</span>Play
        </button>
        <QuestionContainer v-else-if="playData.active" />
    </Transition>
</template>

<script setup lang="ts">
import playData from '@/scripts/play';
import QuestionContainer from '../questions/QuestionContainer.vue';
</script>

<style lang="css" scoped>
.v-enter-from,
.v-leave-to {
    translate: calc(-50% - 100px) 0;
}

.v-enter-to,
.v-leave-from {
    translate: calc(-50%) 0;
}

.v-enter-active,
.v-leave-active {
    transition: 0.5s ease-in-out;
}

.playButton {
    position: absolute;
    left: 50%;
    translate: -50% 0;
}
</style>
