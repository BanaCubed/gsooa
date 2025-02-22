<template>
    <div id="content">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Praesentium, dolor.
        <button onclick="startPlay()">
            <span class="material-symbols-rounded">pan_tool_alt</span>Button
        </button>
    </div>
</template>

<script setup lang="ts">
import { startPlay } from '@/scripts/play';

defineExpose({
    startPlay,
});
</script>

<style lang="css" scoped></style>
