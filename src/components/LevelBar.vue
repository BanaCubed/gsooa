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
    syntax: '<number>';
    inherits: false;
    initial-value: 0;
}

#levelBar {
    width: 350px;
    min-height: 35px;
    background-color: var(--color-background-soft);
    border: 4px solid var(--color-text);
    border-radius: 10px;
    overflow: clip;
}

#levelFill {
    width: v-bind(
        "((playData.score - ((1.1 ** (playData.level - 1)) * 5 * (playData.level - 1))) / ((1.1 ** playData.level) * 5 * playData.level - ((1.1 ** (playData.level - 1)) * 5 * (playData.level - 1))) * 342) + 'px'"
    );
    min-height: 27px;
    background-color: orange;
    border: 0 solid var(--color-text);
    border-radius: 6px;
    transition: width 0.5s cubic-bezier(0.075, 0.82, 0.165, 1);
    animation: levelBar 3s linear infinite 0s;
    background-position-x: left;
    --levelBarProgress: 0;
    background-image: repeating-linear-gradient(
        -45deg,
        transparent calc(calc(var(--levelBarProgress) * -20px) - 10px),
        transparent calc(var(--levelBarProgress) * -20px),
        rgba(255, 255, 255, 0.25) calc(var(--levelBarProgress) * -20px),
        rgba(255, 255, 255, 0.25) calc(calc(var(--levelBarProgress) * -20px) + 10px)
    );
}

@property --levelBarProgress {
    syntax: '<number>';
    initial-value: 0;
    inherits: true;
}

@keyframes levelBar {
    to {
        --levelBarProgress: 1;
    }
    from {
        --levelBarProgress: 0;
    }
}
</style>
