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
      <div v-if="task.end_task_reason !== undefined && task.end_task_reason != ''">
        <span>状态: {{task.task_status}} ({{task.end_task_reason}})</span>
      </div>
      <div v-if="task.detail.cultivate_result.factor_list !== undefined && task.detail.cultivate_result.factor_list.length !== 0">
        因子获取：<span class="mr-1" v-for="factor in task.detail.cultivate_result.factor_list">
          <span v-if="factor[0] === '速度' || factor[0] === '耐力'|| factor[0] === '力量'|| factor[0] === '毅力'|| factor[0] === '智力'"  style="background-color: #49BFF7;" class="badge badge-pill badge-secondary">{{factor[0]}}({{factor[1]}})</span>
          <span v-if="factor[0] === '短距离' || factor[0] === '英里'|| factor[0] === '中距离'|| factor[0] === '长距离'|| factor[0] === '泥地'|| factor[0] === '草地'|| factor[0] === '领跑'|| factor[0] === '跟前'|| factor[0] === '居中'|| factor[0] === '后追'"  style="background-color: #FF78B2;" class="badge badge-pill badge-secondary">{{factor[0]}}({{factor[1]}})</span>
          <span v-if="factor[0] !== '速度' && factor[0] !== '耐力'&& factor[0] !== '力量'&& factor[0] !== '毅力'&& factor[0] !== '智力'&& factor[0] !== '短距离' && factor[0] !== '英里'&& factor[0] !== '中距离'&& factor[0] !== '长距离'&& factor[0] !== '泥地'&& factor[0] !== '草地' &&factor[0] !== '领跑'&& factor[0] !== '跟前'&& factor[0] !== '居中'&& factor[0] !== '后追'" 
            style="background-color: #E0E0E0; color: #794016;" class="badge badge-pill badge-secondary">{{factor[0]}}({{factor[1]}})</span>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import UmamusumeTaskDetailInfo from "@/components/umamusume/UmamusumeTaskDetailInfo.vue";
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