<template>
  <div id="ura-config-modal" class="modal fade" data-backdrop="static" data-keyboard="false">
    <div class="modal-dialog modal-dialog-centered modal-xl">
      <div class="modal-content" @click.stop>
        <h5 class="modal-header">URA配置</h5>
        <div class="modal-body">
          <!-- 技能启发选择额外权重 -->
          <div class="form-group">
            <h5><b>(测试)</b> 支援卡启发(感叹号)选择额外权重</h5>
            <p>支援卡出现启发(感叹号)时为训练选择提供的额外权重。单个训练中的多个感叹号只计算一次权重</p>
            <p>可设置范围[0, 1]。 0表示支援卡启发不对训练选择有任何影响, 1表示一定会选择有启发的训练。</p>
            <div class="row">
              <div class="col-4">
                <div class="form-group">
                  <label for="ura-year1-skill-event-weight">第一年</label>
                  <input 
                    type="number" 
                    v-model="internalSkillEventWeight[0]" 
                    class="form-control" 
                    id="ura-year1-skill-event-weight"
                    @input="onWeightInput(0)"
                    step="0.1"
                    min="0"
                    max="1"
                  >
                </div>
              </div>
              <div class="col-4">
                <div class="form-group">
                  <label for="ura-year2-skill-event-weight">第二年</label>
                  <input 
                    type="number" 
                    v-model="internalSkillEventWeight[1]" 
                    class="form-control" 
                    id="ura-year2-skill-event-weight"
                    @input="onWeightInput(1)"
                    step="0.1"
                    min="0"
                    max="1"
                  >
                </div>
              </div>
              <div class="col-4">
                <div class="form-group">
                  <label for="ura-year3-skill-event-weight">第三年</label>
                  <input 
                    type="number" 
                    v-model="internalSkillEventWeight[2]" 
                    class="form-control" 
                    id="ura-year3-skill-event-weight"
                    @input="onWeightInput(2)"
                    step="0.1"
                    min="0"
                    max="1"
                  >
                </div>
              </div>
            </div>
          </div>
          
          <!-- 重置技能启发权重配置 -->
          <div class="form-group">
            <label for="ura-reset-skill-event-weight-list">学习完以下技能后重置技能启发权重至0</label>
            <textarea 
              type="text" 
              v-model="internalResetSkillEventWeightList" 
              class="form-control" 
              id="ura-reset-skill-event-weight-list" 
              placeholder="技能1名称,技能2名称,....(使用英文逗号)"
              rows="3"
            ></textarea>
          </div>
        </div>
        <div class="modal-footer">
          <span class="btn auto-btn confirm-btn-large" v-on:click="confirm">确认</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UraConfigModal',
  props: {
    show: Boolean,
    skillEventWeight: {
      type: Array,
      default: () => [0, 0, 0]
    },
    resetSkillEventWeightList: {
      type: String,
      default: ''
    },
  },
  emits: ['update:show', 'confirm'],
  data() {
    return {
      internalSkillEventWeight: [...this.skillEventWeight],
      internalResetSkillEventWeightList: this.resetSkillEventWeightList
    };
  },
  watch: {
    show(newVal) {
      if (newVal) {
        // When show becomes true, display the modal
        $('#ura-config-modal').modal({
          backdrop: 'static',
          keyboard: false,
          show: true
        });
      } else {
        // When show becomes false, hide the modal
        $('#ura-config-modal').modal('hide');
      }
    },
    skillEventWeight: {
      handler(newVal) {
        this.internalSkillEventWeight = [...newVal];
      },
      deep: true
    },
    resetSkillEventWeightList(newVal) { 
      this.internalResetSkillEventWeightList = newVal; 
    },
  },
  methods: {
    onWeightInput(index) {
      // 限制输入范围 [0, 1]
      let value = parseFloat(this.internalSkillEventWeight[index]);
      if (value > 1) {
        this.internalSkillEventWeight[index] = 1;
      } else if (value < 0) {
        this.internalSkillEventWeight[index] = 0;
      }
    },
    confirm() {
      // Emit the updated values back to the parent
      this.$emit('confirm', {
        skillEventWeight: this.internalSkillEventWeight.map(Number),
        resetSkillEventWeightList: this.internalResetSkillEventWeightList,
      });
      this.$emit('update:show', false);
      
      this.$nextTick(() => {
        this.restoreParentModalScrolling();
      });
    },
    cancel() {
      this.$emit('update:show', false);
      this.$emit('cancel');
      
      // 确保父modal的滚动功能在关闭时得到恢复
      this.$nextTick(() => {
        this.restoreParentModalScrolling();
      });
    },
    restoreParentModalScrolling() {
      // 恢复父modal的滚动功能
      setTimeout(() => {
        if ($('.modal-open').length > 0) {
          $('body').addClass('modal-open');
          const parentModal = $('#create-task-list-modal');
          if (parentModal.hasClass('show')) {
            const modalBody = parentModal.find('.modal-body');
            if (modalBody.length > 0) {
              modalBody.css('overflow-y', 'auto');
              // 强制触发重新渲染
              modalBody[0].offsetHeight;
            }
          }
        }
      }, 100);
    },
  },
  mounted() {
    // Initialize Bootstrap modal behavior
    $('#ura-config-modal').on('hidden.bs.modal', () => {
      this.$emit('update:show', false);
      // 确保父modal保持滚动功能
      this.$nextTick(() => {
        this.restoreParentModalScrolling();
      });
    });
  }
};
</script>

<style scoped>
/* 确保URA配置modal在最顶层 */
#ura-config-modal.modal {
  z-index: 1060; /* 比TaskEditModal和遮罩层更高 */
}

#ura-config-modal .modal-dialog {
  z-index: 1061;
}

/* 取消按钮样式 */
.cancel-btn {
  background-color: #dc3545 !important;
  color: white !important;
  padding: 0.4rem 0.8rem !important;
  font-size: 1rem !important;
  border-radius: 0.25rem;
  border: none;
  cursor: pointer;
  min-width: 60px;
  min-height: 30px;
  font-weight: 500;
}

.cancel-btn:hover {
  background-color: #c82333 !important;
  color: white !important;
}

/* 放大确认按钮 */
.confirm-btn-large {
  background-color: #0faedf !important;
  color: white !important;
  padding: 0.5rem 1rem !important;
  font-size: 1rem !important;
  font-weight: 400 !important;
  min-width: 60px;
  min-height: 40px;
}

.confirm-btn-large:hover {
  background-color: #1ea7e1 !important;
  color: white !important;
}
</style>
