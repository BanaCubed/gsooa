<script setup lang="ts">
import playData from '@/scripts/play';
</script>

<template>
    <div id="levelBar">
        <div id="levelFill" />
    </div>
</template>

<style lang="css" scoped>
@property --fill {
    syntax: "<number>";
    inherits: false;
    initial-value: 0;
}

#levelBar {
    width: 250px;
    min-height: 20px;
    background-color: var(--color-background-soft);
    border: 4px solid var(--color-text);
    border-radius: 10px;
    overflow: clip;
}

#levelFill {
    width: v-bind("((playData.score - ((1.1 ** (playData.level - 1)) * 5 * (playData.level - 1))) / ((1.1 ** playData.level) * 5 * playData.level - ((1.1 ** (playData.level - 1)) * 5 * (playData.level - 1))) * 250) + 'px'");
    min-height: 12px;
    background-color: orange;
    border: 0 solid var(--color-text);
    border-radius: 10px;
    transition: width 0.5s;
}
</style>
