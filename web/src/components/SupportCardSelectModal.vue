<template>
  <div id="support-card-select-modal" class="modal fade" data-backdrop="static" data-keyboard="false">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h5>支援卡选择</h5>
        </div>
        <div class="modal-body">
          <!-- 目前内容为空 -->
        </div>
        <div class="modal-footer">
          <span class="btn cancel-btn" @click="handleCancel">取消</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SupportCardSelectModal",
  props: {
    show: {
      type: Boolean,
      required: true
    }
  },
  emits: ['update:show', 'cancel'],
  watch: {
    show(newVal) {
      if (newVal) {
        // 显示弹窗
        $('#support-card-select-modal').modal({
          backdrop: 'static',
          keyboard: false,
          show: true
        });
      } else {
        // 隐藏弹窗
        $('#support-card-select-modal').modal('hide');
      }
    }
  },
  methods: {
    handleCancel() {
      this.$emit('update:show', false);
      this.$emit('cancel');
      // 恢复父modal滚动
      this.$nextTick(() => {
        this.restoreParentModalScrolling();
      });
    },
    restoreParentModalScrolling() {
      setTimeout(() => {
        if ($('.modal-open').length > 0) {
          $('body').addClass('modal-open');
          const parentModal = $('#create-task-list-modal');
          if (parentModal.hasClass('show')) {
            const modalBody = parentModal.find('.modal-body');
            if (modalBody.length > 0) {
              modalBody.css('overflow-y', 'auto');
              modalBody[0].offsetHeight;
            }
          }
        }
      }, 100);
    }
  },
  mounted() {
    $('#support-card-select-modal').on('hidden.bs.modal', () => {
      this.$emit('update:show', false);
      this.$nextTick(() => {
        this.restoreParentModalScrolling();
      });
    });
  }
}
</script>

<style scoped>
.cancel-btn {
  background-color: #dc3545 !important;
  color: white !important;
  padding: 0.4rem 0.8rem !important;
  font-size: 1rem !important;
  border-radius: 0.25rem;
  border: none;
  cursor: pointer;
}
.cancel-btn:hover {
  background-color: #c82333 !important;
  color: white !important;
}
/* 保证弹窗在遮罩层之上 */
#support-card-select-modal.modal {
  z-index: 1060;
}
#support-card-select-modal .modal-dialog {
  z-index: 1061;
}
</style>
