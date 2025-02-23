import HomeTab from '@/components/tabs/HomeTab.vue';
import PlayTab from '@/components/tabs/PlayTab.vue';
import SettingsTab from '@/components/tabs/SettingsTab.vue';
import { computed, ref, type ComputedRef } from 'vue';
import type { JSX } from 'vue/jsx-runtime';
import playData from './play';

/*
 This file adapted from one of *my* projects
 All code here written by me, and during the assessment duration
 https://code.incremental.social/banacubed/prisma-rpg/src/branch/main/src/data/tabs/tabs.ts
*/

export enum Tabs {
    Home,
    Settings,
    Play,
}

export enum Subtabs {}

export interface TabButtonData {
    /**
     * The ID of the tab to use. Should be taken with consideration of the enum `Tabs`
     */
    tab: Tabs;
    /**
     * The display name of the tab (appears when hovered). Not to be used for comparisons.
     */
    name: string;
    /**
     * The icon displayed on the tab button. Should be an icon from material icons.
     */
    icon: string;
    /**
     * The color of the tab button.
     */
    color: string;
    /**
     * Element to be rendered whilst the tab is active.
     */
    display: JSX.Element;
    /**
     * A ComputedRef representing whether the tab can be entered.
     */
    active: ComputedRef<boolean>;
}

/**
 * An ordered array that represents the tabs displayed to the user.
 *
 * It is recommended to add new tabs to the start of the array.
 */
export const tabs: TabButtonData[] = [
    {
        // Home
        tab: Tabs.Home,
        name: 'Home',
        icon: 'home',
        color: 'hsl(120, 100%, 17%)',
        display: <HomeTab />,
        active: computed(() => !playData.value.active),
    },
    {
        // Settings
        tab: Tabs.Settings,
        name: 'Settings',
        icon: 'build',
        color: 'hsl(210, 20%, 25%)',
        display: <SettingsTab />,
        active: computed(() => !playData.value.active),
    },
    {
        // Play
        tab: Tabs.Play,
        name: 'Play',
        icon: 'play_arrow',
        color: 'hsl(60, 100%, 15%)',
        display: <PlayTab />,
        active: computed(() => true),
    },
];

/**
 * A `Ref` representing the current tab.
 */
export const tab = ref<Tabs>(Tabs.Home);
export const activeTab = computed(() => tabs.filter((t) => t.tab === tab.value)[0]);
