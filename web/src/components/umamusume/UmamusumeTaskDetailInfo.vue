<template>
  <div>
    <div v-if="task.task_type === 1">
      <div>
        <span>剧本: {{ scenarioName }}</span>
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
  computed: {
    scenarioName() {
      if (this.task.detail?.scenario === 1) {
        return 'URA';
      } else if (this.task.detail?.scenario === 2) {
        return '青春杯';
      }
      // Add more scenarios here as needed
      return '未知剧本';
    }
  }
}
</script>

<style scoped>

</style>