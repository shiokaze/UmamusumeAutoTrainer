<template>
  <div class="row">
    <div class="col-4">
      <div class="part">
        <scheduler-panel v-bind:waiting-task-list="waitingTaskList"
                         v-bind:running-task="runningTask"
                         v-bind:history-task-list="historyTaskList"
                         v-bind:cron-job-list="cronJobList"
        ></scheduler-panel>
      </div>
    </div>
    <div class="col-8">
      <log-panel v-bind:log-content="logContent"></log-panel>
    </div>
  </div>
</template>

<script>
import SchedulerPanel from "../components/SchedulerPanel.vue";
import LogPanel from "../components/base/LogPanel.vue"
export default {
  name: "AutoController",
  components: { LogPanel, SchedulerPanel},
  data() {
    return {
      logId:'0',
      runningTask: undefined,
      waitingTaskList:[],
      historyTaskList:[],
      cronJobList:[],
      taskList:[],
      logContent:"",
    }
  },
  mounted:function() {
    let vue = this;
    setInterval(function () {
      vue.getTaskList();
      vue.getTaskLog()
    },1000)
  },
  methods:{
    getTaskList:function (){
      this.axios.get("/task").then(
          res=>{
            this.taskList = res.data;
            let waitingTaskList = []
            let historyTaskList = []
            let cronJobList = []
            let runningTask = undefined

            this.taskList.forEach(
              t=>{
                if(t['task_execute_mode'] === 1){
                  if(t['task_status'] === 2){
                    runningTask = t
                  }else if (t['task_status'] === 1){
                    waitingTaskList.push(t)
                  }else if (t['task_status'] === 5 || t['task_status'] === 4 || t['task_status'] === 3){
                    historyTaskList.push(t)
                  }
                }else if(t['task_execute_mode'] === 2){
                  if(t['task_status'] === 6||t['task_status'] === 7){
                    cronJobList.push(t)
                  }
                }
              }
            )
            this.waitingTaskList = waitingTaskList
            this.historyTaskList = historyTaskList
            this.runningTask = runningTask
            this.cronJobList = cronJobList
            if(this.runningTask === undefined){
              this.logId = '0'
            }else{
              this.logId = runningTask['task_id']
            }
          }
      );
    },
    getTaskLog:function (){
      if(this.logId !== '0'){
        this.axios.get("/log/"+this.logId).then(
            res=>{
              this.logContent = res.data.data;
            }
        );
      }
    }
  }
}
</script>

<style scoped>

</style>