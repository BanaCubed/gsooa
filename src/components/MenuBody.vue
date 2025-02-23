<template>
    <div id="content">
        <component :is="activeTab.display" />
    </div>
</template>

<script setup lang="ts">
import { activeTab } from '@/scripts/tabs';
import { render } from 'vue';

defineExpose({
    render
})
</script>

<style lang="css" scoped>
#content {
    width: fit-content;
}
</style>
