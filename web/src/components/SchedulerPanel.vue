<template>
  <div>
    <div class="part">
      <auto-status-panel></auto-status-panel>
    </div>
    <!--  执行中任务  -->
    <div class="part">
      <running-task-panel v-bind:running-task="runningTask"></running-task-panel>
    </div>
    <!--  等待队列  -->
    <div class="part">
      <waiting-task-list v-bind:waiting-task-list="waitingTaskList"></waiting-task-list>
    </div>
    <!--  定时队列  -->
    <!-- <div class="part">
      <cron-job-list v-bind:cron-job-list="cronJobList"></cron-job-list>
    </div> -->
    <!--  历史队列  -->
    <div class="part">
      <history-task-list v-bind:history-task-list="historyTaskList"></history-task-list>
    </div>
    <div class="part">
      <task-edit-modal></task-edit-modal>
    </div>
<!--    {{this.taskList}}-->

  </div>
</template>

<script>
import RunningTaskPanel from "@/components/RunningTaskPanel.vue";
import WaitingTaskList from "@/components/WaitingTaskList.vue";
import AutoStatusPanel from "@/components/AutoStatusPanel.vue"
import TaskEditModal from "@/components/TaskEditModal.vue";
import HistoryTaskList from "@/components/HistoryTaskList.vue";
import CronJobList from "@/components/CronJobList.vue";
export default {
  name: "SchedulerPanel",
  components: {CronJobList, HistoryTaskList, TaskEditModal, WaitingTaskList, AutoStatusPanel, RunningTaskPanel},
  props:["runningTask", "waitingTaskList", "historyTaskList", "cronJobList"],
  data:function (){
    return {
    }
  },

}
</script>

<style scoped>

</style>