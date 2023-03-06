<template>
    <div class="">
        <p>测试搜索</p>
        <!-- <h1>params参数---{{ $route.params.keyword }}====={{ keyword }}</h1> -->
        <!-- <h1>query参数---{{ $route.query.k }}====={{ k }}</h1> -->
    </div>
</template>

<script>
export default {
    name: 'Search',
    props:['keyword','k']
}
</script>

<style scoped>

</style>
