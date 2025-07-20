<template>
  <div id="support-card-select-modal" class="modal fade" data-backdrop="static" data-keyboard="false">
    <div class="modal-dialog modal-dialog-centered modal-xl">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h5>借用支援卡选择</h5>
        </div>
        <div class="modal-body support-card-modal-body">
          <div class="type-btn-row">
            <button
              v-for="type in supportCardTypes"
              :key="type.name"
              type="button"
              class="type-btn"
              :class="{ active: activeType === type.name }"
              @click="setActiveType(type.name)"
            >
              <img :src="type.img" :alt="type.name" class="type-btn-img" />
            </button>
          </div>
          <hr class="type-btn-divider"/>
          <!-- 支援卡图片展示区域 -->
          <div class="support-card-img-grid mt-3">
            <div v-for="row in filteredCardImageRows" :key="row[0].id" class="img-row">
              <div
                v-for="card in row"
                :key="card.id"
                class="img-cell"
                :style="{ flex: '0 0 12.5%' }"
              >
                <div class="img-content">
                  <div
                    class="card-img-wrapper"
                    :class="{ 'selected-card': selectedCard && selectedCard.id === card.id }"
                    @click="selectCard(card)"
                    style="cursor: pointer;"
                  >
                    <img
                      :src="getCardImgUrl(card.id)"
                      :alt="card.name"
                      class="support-card-img"
                      :title="renderSupportCardText(card)"
                      @error="handleImgError"
                    />
                    <!-- 左上角SSR图标 -->
                    <img
                      :src="getRarityIcon('SSR')"
                      class="card-ssr-icon"
                      alt="SSR"
                    />
                    <!-- 右上角类型图标 -->
                    <img
                      :src="getTypeIcon(card.id)"
                      class="card-type-icon"
                      alt="type"
                    />
                  </div>
                  <div class="support-card-label">
                    {{ renderSupportCardTextEllipsis(card) }}
                  </div>
                </div>
              </div>
              <!-- 补齐空位，保证最后一行图片对齐 -->
              <div
                v-for="n in (8 - row.length)"
                :key="'empty-'+n"
                class="img-cell"
                :style="{ flex: '0 0 12.5%' }"
              ></div>
            </div>
          </div>
        </div>
        <div class="modal-footer support-card-modal-footer">
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
      selectedCard: null,
      supportCardTypes: [
        { name: 'speed', img: new URL('../assets/img/support_cards/types/speed.png', import.meta.url).href },
        { name: 'stamina', img: new URL('../assets/img/support_cards/types/stamina.png', import.meta.url).href },
        { name: 'power', img: new URL('../assets/img/support_cards/types/power.png', import.meta.url).href },
        { name: 'will', img: new URL('../assets/img/support_cards/types/will.png', import.meta.url).href },
        { name: 'intelligence', img: new URL('../assets/img/support_cards/types/intelligence.png', import.meta.url).href }
      ],
      activeType: 'speed', // 默认速度
    }
  },
  computed: {
    filteredSupportCardList() {
      // 根据activeType筛选支援卡
      if (this.activeType === 'speed') {
        return this.umamusumeSupportCardList.filter(card => card.id >= 10000 && card.id < 20000);
      } else if (this.activeType === 'stamina') {
        return this.umamusumeSupportCardList.filter(card => card.id >= 20000 && card.id < 30000);
      } else if (this.activeType === 'power') {
        return this.umamusumeSupportCardList.filter(card => card.id >= 30000 && card.id < 40000);
      } else if (this.activeType === 'will') {
        return this.umamusumeSupportCardList.filter(card => card.id >= 40000 && card.id < 50000);
      } else if (this.activeType === 'intelligence') {
        return this.umamusumeSupportCardList.filter(card => card.id >= 50000 && card.id < 60000);
      }
      return [];
    },
    filteredCardImageRows() {
      // 每行8张图片
      const cards = this.filteredSupportCardList;
      const rows = [];
      for (let i = 0; i < cards.length; i += 8) {
        rows.push(cards.slice(i, i + 8));
      }
      return rows;
    },
    cardImageRows() {
      // 每行8张图片
      const cards = this.umamusumeSupportCardList;
      const rows = [];
      for (let i = 0; i < cards.length; i += 8) {
        rows.push(cards.slice(i, i + 8));
      }
      return rows;
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
    },
    getCardImgUrl(id) {
      return new URL(`../assets/img/support_cards/cards/${id}.png`, import.meta.url).href;
    },
    getRarityIcon(rarity){
        // 现在只有SSR
        return new URL('../assets/img/support_cards/rarity/SSR.png', import.meta.url).href;
    },
    handleImgError(event) {
      event.target.src = new URL('../assets/img/support_cards/cards/default.png', import.meta.url).href;
    },
    renderSupportCardText(card) {
      if (!card) return '';
      let type = '';
      if (card.id >= 10000 && card.id < 20000) type = '速';
      else if (card.id >= 20000 && card.id < 30000) type = '耐';
      else if (card.id >= 30000 && card.id < 40000) type = '力';
      else if (card.id >= 40000 && card.id < 50000) type = '根';
      else if (card.id >= 50000 && card.id < 60000) type = '智';
      if (type) {
        return `【${card.name}】${type}·${card.desc}`;
      } else {
        return `【${card.name}】${card.desc}`;
      }
    },
    renderSupportCardTextEllipsis(card) {
      if (!card) return '';
      const imgWidth = 120; // px
      const name = card.name;
      // 计算整体宽度
      let totalWidth = 0;
      let charWidth = [];
      for (let i = 0; i < name.length; i++) {
        const width = /[A-Za-z0-9]/.test(name[i]) ? 7 : 13;
        totalWidth += width;
        charWidth.push(width);
      }
      // 如果宽度足够，直接返回
      if (totalWidth <= imgWidth) {
        let type = '';
        if (card.id >= 10000 && card.id < 20000) type = '速';
        else if (card.id >= 20000 && card.id < 30000) type = '耐';
        else if (card.id >= 30000 && card.id < 40000) type = '力';
        else if (card.id >= 40000 && card.id < 50000) type = '根';
        else if (card.id >= 50000 && card.id < 60000) type = '智';
        if (type) {
          return `${name}\n${type}·${card.desc}`;
        } else {
          return `${name}\n${card.desc}`;
        }
      }
      // 需要省略
      // 计算省略号宽度
      const ellipsis = '...';
      const ellipsisWidth = 3 * 3;
      // 计算需要去掉多少字符
      let left = Math.ceil(name.length/2)-1;
      let right = name.length - left - 1;

      while (totalWidth + ellipsisWidth > imgWidth){
        totalWidth -= charWidth[left];
        totalWidth -= charWidth[right];
        left--;
        right++;
      }

      const leftStr = name.slice(0, left + 1);
      const rightStr = name.slice(right);
      let type = '';
      if (card.id >= 10000 && card.id < 20000) type = '速';
      else if (card.id >= 20000 && card.id < 30000) type = '耐';
      else if (card.id >= 30000 && card.id < 40000) type = '力';
      else if (card.id >= 40000 && card.id < 50000) type = '根';
      else if (card.id >= 50000 && card.id < 60000) type = '智';
      if (type) {
        return `${leftStr}${ellipsis}${rightStr}\n${type}·${card.desc}`;
      } else {
        return `${leftStr}${ellipsis}${rightStr}\n${card.desc}`;
      }
    },
    setActiveType(type) {
      this.activeType = type;
    },
    getTypeIcon(id) {
      if (id >= 10000 && id < 20000) return new URL('../assets/img/support_cards/types/speed.png', import.meta.url).href;
      if (id >= 20000 && id < 30000) return new URL('../assets/img/support_cards/types/stamina.png', import.meta.url).href;
      if (id >= 30000 && id < 40000) return new URL('../assets/img/support_cards/types/power.png', import.meta.url).href;
      if (id >= 40000 && id < 50000) return new URL('../assets/img/support_cards/types/will.png', import.meta.url).href;
      if (id >= 50000 && id < 60000) return new URL('../assets/img/support_cards/types/intelligence.png', import.meta.url).href;
      return '';
    },
    selectCard(card) {
      this.selectedCard = card;
    },
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
  min-width: 60px;
  min-height: 30px;
  font-weight: 500;
}
.cancel-btn:hover {
  background-color: #c82333 !important;
  color: white !important;
}
.auto-btn {
  background-color: #0faedf !important;
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
.auto-btn:hover {
  background-color: #1ea7e1 !important;
  color: white !important;
}
/* 保证弹窗在遮罩层之上 */
#support-card-select-modal.modal {
  z-index: 1060;
}
#support-card-select-modal .modal-dialog {
  z-index: 1061;
}
.support-card-modal-body {
  max-height: 600px;
  overflow-y: auto;
  /* 让footer固定时，body不被footer遮挡 */
  padding-bottom: 80px;
}
.support-card-modal-footer {
  position: sticky;
  bottom: 0;
  background: #fff;
  z-index: 2;
  box-shadow: 0 -2px 8px rgba(0,0,0,0.04);
  display: flex;
  justify-content: flex-end;
  gap: 8px;
  /* 保证footer始终在底部 */
  padding-top: 16px;
  padding-bottom: 16px;
}
.support-card-img-grid {
  display: flex;
  flex-direction: column;
  gap: 2px;
  margin-bottom: 8px;
}
.img-row {
  display: flex;
  flex-direction: row;
  gap: 0px;
  margin-bottom: 0;
}
.img-cell {
  flex: 0 0 12.5%; /* 一行8张图片 */
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 0;
  padding: 0 2px;
}
.img-content {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.card-img-wrapper {
  position: relative;
  display: inline-block;
}
.card-img-wrapper.selected-card {
  box-shadow: none;
  border-radius: 10px;
}
.card-img-wrapper.selected-card::after {
  content: '';
  position: absolute;
  left: 0; top: 0;
  width: 101%; height: 98%;
  background: rgba(0, 0, 0, 0.5); /* 半透明黑色蒙层 */
  border-radius: 10px;
  z-index: 3;
  pointer-events: none;
}
.card-img-wrapper.selected-card::before {
  content: '';
  position: absolute;
  left: 50%; top: 50%;
  width: 48px;
  height: 36px;
  background: url('/src/assets/img/support_cards/selected_check.svg') center center no-repeat;
  background-size: contain;
  transform: translate(-50%, -50%);
  z-index: 4;
  pointer-events: none;
}
.card-ssr-icon {
  position: absolute;
  top: 6px; /* 往下挪，避免超出图片边界 */
  left: 10px;
  width: 30px;
  height: 30px;
  z-index: 2;
  pointer-events: none;
}
.card-type-icon {
  position: absolute;
  top: 4px; /* 往下挪，避免超出图片边界 */
  right: 2px;
  width: 28px;
  height: 28px;
  z-index: 2;
  pointer-events: none;
}
.support-card-label {
  margin-top: 4px;
  font-size: 0.84rem;
  color: #333;
  text-align: center;
  word-break: break-all;
  line-height: 1.2;
  max-width: 125px; /* 与图片宽度保持一致 */
  min-height: 1.2em;
  white-space: pre-line;
  overflow: hidden;
  text-overflow: ellipsis;
  display: block;
}
.support-card-img {
  width: 120px;
  height: 160px;
  object-fit: cover;
  border-radius: 8px;
  border: 1px solid #eee;
  box-shadow: 0 1px 4px rgba(0,0,0,0.08);
  background: #fafafa;
  margin-top: 4px;
  margin-bottom: 4px;
  display: block;
}
.type-btn-row {
  display: flex;
  justify-content: flex-start; /* 靠左对齐 */
  align-items: center;
  gap: 8px;
  margin-top: 12px;
  margin-bottom: 8px;
}
.type-btn {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  outline: none;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.type-btn-img {
  width: 32px;
  height: 32px;
  object-fit: contain;
  display: block;
}
.type-btn-divider {
  border: none;
  border-top: 1px solid #e0e0e0;
  margin: 0 0 12px 0;
}
.type-btn.active {
  border: 2px solid #3485E3;
  border-radius: 8px;
  background: #f0f6ff;
}
</style>
