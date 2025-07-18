<template>
  <div id="support-card-select-modal" class="modal fade" data-backdrop="static" data-keyboard="false">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h5>支援卡选择</h5>
        </div>
        <div class="modal-body">
          <div class="form-group">
            <label for="supportCardSelect">选择支援卡</label>
            <select v-model="selectedCard" class="form-control" id="supportCardSelect">
              <option v-for="card in umamusumeSupportCardList" :key="card.id" :value="card">
                ({{card.desc}}) {{card.name}}
              </option>
            </select>
          </div>
        </div>
        <div class="modal-footer">
          <span class="btn cancel-btn" @click="handleCancel">取消</span>
          <span class="btn auto-btn" style="margin-left:8px;" @click="handleConfirm">确认</span>
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
  emits: ['update:show', 'cancel', 'confirm'],
  data() {
    return {
      umamusumeSupportCardList: [
        {id:10001, name:'在耀眼景色的前方', desc:'无声铃鹿'},
        {id:10002, name:'有梦想就要大声说出来！', desc:'东海帝王'},
        {id:10003, name:'Run(my)way', desc:'黄金城'},
        {id:10004, name:'好快！好吃！好快', desc:'樱花进王'},
        {id:10005, name:'哪怕还不能独当一面', desc:'西野花'},
        {id:10006, name:'必杀技！双胡萝卜拳', desc:'微光飞驹'},
        {id:10007, name:'夕阳是憧憬之色', desc:'特别周'},
        {id:10008, name:'涡轮引擎马力全开！', desc:'双涡轮'},
        {id:10009, name:'身后迫近的热浪是动力', desc:'北部玄驹'},
        {id:10010, name:'身为新娘！', desc:'川上公主'},
        {id:10011, name:'Two Pieces', desc:'成田白仁'},
        {id:10012, name:'独享冰凉？', desc:'东商变革'},
        {id:10013, name:'优俊王传说·登上最强宝座', desc:'黄金船'},
        {id:10014, name:'被授予魔力的英雄', desc:'荒漠英雄'},
        {id:10015, name:'队形: PARTY', desc:'重炮'},
        {id:10016, name:'追寻未曾见过的景色', desc:'无声铃鹿'},
        {id:10017, name:'萍水相逢即是福', desc:'待兼福来'},
        {id:10018, name:'In my way', desc:'岛川乔丹'},

        {id:20001, name:'不沉舰的进击', desc:'黄金船'},
        {id:20002, name:'期待已久的计谋', desc:'青云天空'},
        {id:20003, name:'划破天空的闪电少女！', desc:'玉藻十字'},
        {id:20004, name:'一颗安心糖', desc:'超级溪流'},
        {id:20005, name:'身为王牌', desc:'目白麦昆'},
        {id:20006, name:'幸福漫天飞舞的时刻', desc:'米浴'},
        {id:20007, name:'超越那前方的背影', desc:'里见光钻'},
        {id:20008, name:'樱花盛开之时', desc:'樱花千代王'},
        {id:20009, name:'43、8、1', desc:'中山庆典'},
        {id:20010, name:'全力嬉闹！', desc:'胜利奖券'},
        {id:20011, name:'WINNING DREAM', desc:'无声铃鹿'},
        {id:20012, name:'鸣箭嗤天', desc:'成田白仁'},
        {id:20013, name:'独奏·螺旋卡农', desc:'曼城茶座'},
        {id:20014, name:'想要飞奔而出的心情', desc:'名将怒涛'},

        {id:30001, name:'伏特加之路', desc:'伏特加'},
        {id:30002, name:'热情的冠军！', desc:'神鹰'},
        {id:30003, name:'这就是我的优俊偶像之道', desc:'醒目飞鹰'},
        {id:30004, name:'要受人喜爱啊', desc:'小栗帽'},
        {id:30005, name:'心中的烈火无法抑制', desc:'八重无敌'},
        {id:30006, name:'梦想真的可以实现！', desc:'胜利奖券'},
        {id:30007, name:'幸福就在转角后', desc:'米浴'},
        {id:30008, name:'Head-on fight！', desc:'青竹回忆'},
        {id:30009, name:'Trifle Vacation', desc:'大和赤骥'},
        {id:30010, name:'起舞今宵', desc:'帝王光辉'},
        {id:30011, name:'大闹万圣夜！', desc:'玉藻十字'},
        {id:30012, name:'舞动吧·躁动吧·狂欢吧！', desc:'大拓太阳神'},
        {id:30013, name:'冰晶之日', desc:'美丽周日'},
        {id:30014, name:'夜有黎明，天有祥星', desc:'爱慕织姬'},
        {id:30015, name:'存在于此的幸福', desc:'爱丽数码'},

        {id:40001, name:'献上全国第一的演出', desc:'特别周'},
        {id:40002, name:'万紫千红中一枝独秀', desc:'草上飞'},
        {id:40003, name:'飞奔吧，闪耀吧', desc:'艾尼风神'},
        {id:40004, name:'B·N·Winner！', desc:'胜利奖券'},
        {id:40005, name:'乌菈菈～的休息日', desc:'春乌菈菈'},
        {id:40006, name:'尽管笑我傻吧', desc:'目白善信'},
        {id:40007, name:'Just keep going.', desc:'待兼唐怀瑟'},
        {id:40008, name:'请品尝第一口！', desc:'菱曙'},
        {id:40009, name:'爽快！决胜一击！', desc:'目白莱恩'},
        {id:40010, name:'内心双脚皆温暖', desc:'生野狄杜斯'},
        {id:40011, name:'点亮初宵的奉纳舞', desc:'雪之美人'},
        {id:40012, name:'极快！最快！花之风暴！', desc:'樱花进王'},

        {id:50001, name:'全身心的感谢', desc:'美妙姿势'},
        {id:50002, name:'冲向前方7厘米之外', desc:'空中神宫'},
        {id:50003, name:'由故乡直达的助威！', desc:'雪之美人'},
        {id:50004, name:'心与心愿', desc:'目白多伯'},
        {id:50005, name:'即使满身泥土，也要追逐梦想', desc:'优秀素质'},
        {id:50006, name:'明天全国都会染红吧', desc:'青云天空'},
        {id:50007, name:'幽灵小姐与万圣节的魔法', desc:'美浦波旁'},
        {id:50008, name:'可爱的你，美丽的你', desc:'真机怜'},
        {id:50009, name:'倔强的集市', desc:'成田大进'},
        {id:50010, name:'饱含心意的纸杯蛋糕', desc:'西野花'},
      ],
      selectedCard: null
    }
  },
  watch: {
    show(newVal) {
      if (newVal) {
        // 显示弹窗
        $('#support-card-select-modal').modal({
          backdrop: 'static',
          keyboard: false,
          show: true
        });
        // 默认选中第一个
        if (!this.selectedCard) {
          this.selectedCard = this.umamusumeSupportCardList[0];
        }
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
    handleConfirm() {
      this.$emit('confirm', this.selectedCard);
      this.$emit('update:show', false);
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
