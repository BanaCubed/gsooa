<script setup lang="ts">
import playData from '@/scripts/play';

</script>

<template>
    {{ playData.currentQuestion.variables[0] }} + {{ playData.currentQuestion.variables[1] }} = ?
</template>
