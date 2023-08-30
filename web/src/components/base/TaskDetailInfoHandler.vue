<template>
  <div>
    <div v-if="task.app_name === 'umamusume'">
      <div>
        <span v-if="task.task_start_time !== undefined" class="small time">{{task.task_start_time}}</span>
        <span v-if="task.end_task_time !== undefined" class="small time"> ~ {{task.end_task_time}}</span>
        <span v-if= "task.task_start_time === undefined" class="small time">未开始</span>
        <div v-if="task.task_execute_mode === 'CRON_JOB'" class="small time">下次执行时间：{{task.cron_job_info?.next_time}} ({{task.cron_job_info?.cron}})</div>
      </div>
      <div class="btn-group float-right" role="group" aria-label="Basic example">
        <button type="button" class="btn auto-btn" v-on:click="resetTask">重置</button>
        <button type="button" class="btn auto-btn" v-on:click="deleteTask">删除</button>
      </div>
      <UmamusumeTaskDetailInfo :task="task"></UmamusumeTaskDetailInfo>
      <div v-if="task.end_task_reason !== undefined">
        <span>状态: {{task.task_status}} ({{task.end_task_reason}})</span>
      </div>
    </div>
  </div>
</template>

<script>
import UmamusumeTaskDetailInfo from "../umamusume/UmamusumeTaskDetailInfo.vue";
export default {
  name: "TaskDetailInfoHandler",
  components: {UmamusumeTaskDetailInfo},
  props: ["task"],
  methods: {
    resetTask: function (){
      let payload = {
        task_id: this.task.task_id
      }
      console.log(JSON.stringify(payload))
      this.axios.post("/action/bot/reset-task", JSON.stringify(payload)).then()
    },
    deleteTask: function (){
      let payload = {
        task_id: this.task.task_id
      }
      console.log(JSON.stringify(payload))
      this.axios.delete("/task", JSON.stringify(payload)).then()
    },
  }
}
</script>

<style scoped>
.time{
  color: #999;
}
</style>