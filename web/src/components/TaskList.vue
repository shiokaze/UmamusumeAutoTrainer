<template>
  <div>
    <div v-if="taskList === undefined || taskList.length === 0">
      <div class="card-body">
        {{noDataLabel}}
      </div>
    </div>
    <div v-if="taskList !== undefined">
      <ul class="list-group list-group-flush">
        <li v-for="task in taskList" class="list-group-item">
          <div class="part">
            <div class="d-flex bd-highlight">
              <h5 class="card-title">{{task['task_desc']}}</h5>
            </div>
            <task-detail-info-handler :task="task"></task-detail-info-handler>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import TaskDetailInfoHandler from "./base/TaskDetailInfoHandler.vue";
export default {
  name: "TaskList",
  components: {TaskDetailInfoHandler},
  props:["taskList", "noDataLabel"],
  data:function (){
    return {
    }
  }
}
</script>

<style scoped>
.card-title{
  margin-bottom: 0;
}
.start-time{
  color: #999;
}
.list-group-item{
  padding: 10px;
}
</style>