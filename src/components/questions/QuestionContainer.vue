<template>
    <div id="questionContainer">
        L1 | Q1<br />
        1 + 1 = ?
    </div>
</template>

<style lang="css" scoped>
#questionContainer:not(.v-enter-active):not(.v-leave-active) {
    translate: -50% 0;
}

#questionContainer {
    position: absolute;
    left: 50%;
}
</style>
