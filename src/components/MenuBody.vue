<template>
    <div id="content">
        <component :is="activeTab.display" />
    </div>
</template>

<script setup lang="ts">
import { activeTab } from '@/scripts/tabs';
</script>

<style lang="css" scoped>
#content {
    width: 100vw;
    overflow-x: clip;
    overflow-y: auto;
    height: calc(100vh - 50px);
    position: absolute;
    bottom: 0;
    left: 0;
    text-align: center;
    padding: 2rem;
}
</style>
