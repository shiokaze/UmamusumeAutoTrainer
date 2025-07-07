<template>
  <div id="aoharu-config-modal" class="modal fade">
    <div class="modal-dialog modal-dialog-centered modal-xl">
      <div class="modal-content">
        <h5 class="modal-header">青春杯配置</h5>
        <div class="modal-body">
          <div class="row">
            <div class="col-5" style="border-right: 1px solid #e0e0e0;">
              <h5>选择预赛选手</h5>
              <div class="form-group">
                <label>预赛第一轮&nbsp;&nbsp;</label>
                <div class="form-check form-check-inline">
                  <input class="form-check-input" type="radio" id="pr1_1" value=1 v-model="preliminaryRound1Selection">
                  <label class="form-check-label" for="pr1_1">1</label>
                </div>
                <div class="form-check form-check-inline">
                  <input class="form-check-input" type="radio" id="pr1_2" value=2 v-model="preliminaryRound1Selection">
                  <label class="form-check-label" for="pr1_2">2</label>
                </div>
                <div class="form-check form-check-inline">
                  <input class="form-check-input" type="radio" id="pr1_3" value=3 v-model="preliminaryRound1Selection">
                  <label class="form-check-label" for="pr1_3">3</label>
                </div>
              </div>
              <div class="form-group">
                <label>预赛第二轮&nbsp;&nbsp;</label>
                <div class="form-check form-check-inline">
                  <input class="form-check-input" type="radio" id="pr2_1" value=1 v-model="preliminaryRound2Selection">
                  <label class="form-check-label" for="pr2_1">1</label>
                </div>
                <div class="form-check form-check-inline">
                  <input class="form-check-input" type="radio" id="pr2_2" value=2 v-model="preliminaryRound2Selection">
                  <label class="form-check-label" for="pr2_2">2</label>
                </div>
                <div class="form-check form-check-inline">
                  <input class="form-check-input" type="radio" id="pr2_3" value=3 v-model="preliminaryRound2Selection">
                  <label class="form-check-label" for="pr2_3">3</label>
                </div>
              </div>
              <div class="form-group">
                <label>预赛第三轮&nbsp;&nbsp;</label>
                <div class="form-check form-check-inline">
                  <input class="form-check-input" type="radio" id="pr3_1" value=1 v-model="preliminaryRound3Selection">
                  <label class="form-check-label" for="pr3_1">1</label>
                </div>
                <div class="form-check form-check-inline">
                  <input class="form-check-input" type="radio" id="pr3_2" value=2 v-model="preliminaryRound3Selection">
                  <label class="form-check-label" for="pr3_2">2</label>
                </div>
                <div class="form-check form-check-inline">
                  <input class="form-check-input" type="radio" id="pr3_3" value=3 v-model="preliminaryRound3Selection">
                  <label class="form-check-label" for="pr3_3">3</label>
                </div>
              </div>
              <div class="form-group">
                <label>预赛第四轮&nbsp;&nbsp;</label>
                <div class="form-check form-check-inline">
                  <input class="form-check-input" type="radio" id="pr4_1" value=1 v-model="preliminaryRound4Selection">
                  <label class="form-check-label" for="pr4_1">1</label>
                </div>
                <div class="form-check form-check-inline">
                  <input class="form-check-input" type="radio" id="pr4_2" value=2 v-model="preliminaryRound4Selection">
                  <label class="form-check-label" for="pr4_2">2</label>
                </div>
                <div class="form-check form-check-inline">
                  <input class="form-check-input" type="radio" id="pr4_3" value=3 v-model="preliminaryRound4Selection">
                  <label class="form-check-label" for="pr4_3">3</label>
                </div>
              </div>
            </div>
            <div class="col-7">
              <h5>选择青春杯队名</h5>
              <div class="form-group">
                <div class="form-check mb-3 ps-0">
                  <input class="form-check-input" type="radio" id="team_taiki" value=1 v-model="aoharuTeamSelection">
                  <label class="form-check-label" for="team_taiki">大树快车 &lt;HOP CHEERS&gt; <SkillIcon name="英里统治者" type="speed"></SkillIcon></label>
                </div>
                <div class="form-check mb-3 ps-0">
                  <input class="form-check-input" type="radio" id="team_fukukitaru" value=2 v-model="aoharuTeamSelection">
                  <label class="form-check-label" for="team_fukukitaru">待兼福来 &lt;晴天跑者&gt; <SkillIcon name="千里眼" type="sight"></SkillIcon></label>
                </div>
                <div class="form-check mb-3 ps-0">
                  <input class="form-check-input" type="radio" id="team_urara" value=3 v-model="aoharuTeamSelection">
                  <label class="form-check-label" for="team_urara">春乌拉拉 &lt;胡萝卜布丁&gt; <SkillIcon name="不屈之心" type="stamina"></SkillIcon></label>
                </div>
                <div class="form-check mb-3 ps-0">
                  <input class="form-check-input" type="radio" id="team_raisu" value=4 v-model="aoharuTeamSelection">
                  <label class="form-check-label" for="team_raisu">米浴 &lt;花开&gt; <SkillIcon name="冷却" type="stamina"></SkillIcon></label>
                </div>
                <div class="form-check mb-3 ps-0">
                  <input class="form-check-input" type="radio" id="team_default" value=5 v-model="aoharuTeamSelection">
                  <label class="form-check-label" for="team_default">默认 &lt;胡萝卜&gt; <SkillIcon name="不停步的女孩" type="accelerate"></SkillIcon></label>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <span class="btn auto-btn" v-on:click="confirm">确定</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SkillIcon from './SkillIcon.vue';

export default {
  name: 'AoharuConfigModal',
  components: {
    SkillIcon
  },
  props: {
    show: Boolean,
    preliminaryRound1Selection: [String, Number],
    preliminaryRound2Selection: [String, Number],
    preliminaryRound3Selection: [String, Number],
    preliminaryRound4Selection: [String, Number],
    aoharuTeamSelection: [String, Number],
  },
  emits: ['update:show', 'confirm'],
  data() {
    return {
      // Internal data for the modal, initialized from props
      internalPreliminaryRound1Selection: this.preliminaryRound1Selection,
      internalPreliminaryRound2Selection: this.preliminaryRound2Selection,
      internalPreliminaryRound3Selection: this.preliminaryRound3Selection,
      internalPreliminaryRound4Selection: this.preliminaryRound4Selection,
      internalAoharuTeamSelection: this.aoharuTeamSelection,
    };
  },
  watch: {
    show(newVal) {
      if (newVal) {
        // When show becomes true, display the modal
        $('#aoharu-config-modal').modal('show');
      } else {
        // When show becomes false, hide the modal
        $('#aoharu-config-modal').modal('hide');
      }
    },
    // Watch for changes in props and update internal data
    preliminaryRound1Selection(newVal) { this.internalPreliminaryRound1Selection = newVal; },
    preliminaryRound2Selection(newVal) { this.internalPreliminaryRound2Selection = newVal; },
    preliminaryRound3Selection(newVal) { this.internalPreliminaryRound3Selection = newVal; },
    preliminaryRound4Selection(newVal) { this.internalPreliminaryRound4Selection = newVal; },
    aoharuTeamSelection(newVal) { this.internalAoharuTeamSelection = newVal; },
  },
  methods: {
    confirm() {
      // Emit the updated values back to the parent
      this.$emit('confirm', {
        preliminaryRound1Selection: this.internalPreliminaryRound1Selection,
        preliminaryRound2Selection: this.internalPreliminaryRound2Selection,
        preliminaryRound3Selection: this.internalPreliminaryRound3Selection,
        preliminaryRound4Selection: this.internalPreliminaryRound4Selection,
        aoharuTeamSelection: this.internalAoharuTeamSelection,
      });
      this.$emit('update:show', false); // Close the modal
    },
  },
  mounted() {
    // Initialize Bootstrap modal behavior
    $('#aoharu-config-modal').on('hidden.bs.modal', () => {
      this.$emit('update:show', false);
    });
  }
};
</script>

<style scoped>
/* Add any specific styles for this modal here */
</style>
