<template>
  <div>
    <div v-if="task.task_type === 1">
      <div>
        <span>剧本: URA</span>
      </div>
      <div>
        <span>目标数值: {{task.detail?.expect_attribute}}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UmamusumeTaskDetailInfo",
  props: ["task"],
}
</script>

<style scoped>

</style>