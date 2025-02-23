<!--
 This file adapted from one of *my* projects
 All code here written by me, and during the assessment duration
 https://code.incremental.social/banacubed/prisma-rpg/src/branch/main/src/data/tabs/Header.vue
 -->

<template>
    <div id="header">
        <div id="tabs">
            <button
                v-for="tabButton in tabs"
                :key="tabButton.name"
                :disabled="!tabButton.active.value"
                :aria-label="tabButton.name"
                :class="{ menuButton: true, activeTab: tab === tabButton.tab }"
                :style="{
                    '--background': tabButton.active.value ? tabButton.color : 'hsl(0, 0%, 10%)',
                    '--length': tabButton.name.length,
                }"
                v-on:click="
                    () => {
                        tab = tabButton.tab;
                    }
                "
            >
                <span class="material-symbols-rounded">{{ tabButton.icon }}</span>
            </button>
            <div id="tabName">
                <Transition>
                    <div :key="activeTab.name" class="tabName">
                        {{ activeTab.name }}
                    </div>
                </Transition>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { activeTab, tab, tabs } from '@/scripts/tabs';
</script>

<style lang="css" scoped>
#header {
    position: fixed;
    display: block;
    width: 100vw;
    background-color: var(--color-background-soft);
    top: 0;
    left: 0;
    height: 50px;
    padding: 3px 10px 10px 15px;
    font-size: 2em;
}

.v-enter-from,
.v-leave-to {
    translate: 0 -50px;
}

.v-enter-to,
.v-leave-from {
    translate: 0 0px;
}

.v-enter-active,
.v-leave-active {
    transition: 0.5s ease-in-out;
}

#tabs {
    display: flex;
    position: absolute;
    right: 0px;
    top: 0px;
    flex-direction: row-reverse;
}

#tabName {
    font-size: 0.7em;
    z-index: -1;
    position: relative;
    margin-right: 0px;
}

#tabName > .tabName {
    position: absolute;
    clip-path: polygon(0 0, calc(100% - 12px) 0, 100% 100%, 12px 100%);
    margin-left: 5px;
    margin-right: -18px;
    padding-left: 20px;
    padding-right: 20px;
    padding-top: 3.2px;
    height: 40px;
    background-color: var(--color-background-mute);
    top: 0px;
    right: 0px;
    font-weight: 700;
}

.menuButton {
    margin-left: 5px;
    margin-right: -21px;
    padding-left: 20px;
    padding-right: 20px;
    height: 50px;
    background-color: var(--background);
    border: none;
    color: var(--color-text);
    min-width: 72px;
    width: 72px;
    overflow: clip;
    font-size: 1em;
    clip-path: polygon(0 0, calc(100% - 15px) 0, 100% 100%, 15px 100%);
    box-shadow: 0 -99px 0 -100px rgba(255, 255, 255, 0.125) inset;
    cursor: pointer;
    transition: 0.5s cubic-bezier(0.075, 0.82, 0.165, 1);
    display: flex;
    flex-direction: row-reverse;
    align-items: center;
    text-shadow: 0 0 5px black;
    position: relative;
    border-radius: 0;
}

.menuButton:disabled {
    color: rgb(from var(--color-text) r g b / 0.3);
    pointer-events: none;
}

.menuButton:disabled .material-symbols-rounded {
    font-variation-settings:
        'opsz' 33,
        'FILL' 0;
    font-size: 1.1em;
}

.menuButton .material-symbols-rounded {
    font-size: 1.3em;
    display: block;
    margin: 0px;
    font-variation-settings:
        'opsz' 39,
        'FILL' 1;
    transition: all 0.5s cubic-bezier(0.075, 0.82, 0.165, 1);
}

.menuButton.activeTab {
    box-shadow: 0 -106px 0 -100px rgba(255, 255, 255, 0.125) inset;
}

.menuButton:hover {
    box-shadow: 0 -151px 0 -100px rgba(255, 255, 255, 0.125) inset;
}

.menuButton:first-child {
    clip-path: polygon(0 0, 100% 0, 100% 100%, 15px 100%);
    margin-right: 0px;
    padding-right: 7px;
    min-width: 57px;
    width: 57px;
}

#tabs > .menuButton:first-child {
    min-width: 72px;
    width: 72px;
    padding-right: 20px;
}
</style>
