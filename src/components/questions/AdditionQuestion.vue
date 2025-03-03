<template>
    <span class="number">{{ playData.currentQuestion.variables[0] }}</span> +
    <span class="number">{{ playData.currentQuestion.variables[1] }}</span> = ?
</template>

<script setup lang="ts">
import playData from '@/scripts/play';
</script>

<style lang="css" scoped>
.number {
    font-weight: 600;
}
</style>
