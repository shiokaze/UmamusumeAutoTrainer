<template>
  <div class="skill-icon">
    <img :src="iconSrc" :alt="name + ' icon'" />
    <span class="skill-name">{{ name }}</span>
  </div>
</template>

<script>
export default {
  name: 'SkillIcon',
  props: {
    type: {
      type: String,
      default: ''
    },
    name: {
      type: String,
      default: '默认技能名称'
    }
  },
  computed: {
    iconSrc() {
      if (this.type === 'speed') {
        return new URL('../assets/img/skills/speed.png', import.meta.url).href;
      } else if (this.type === 'stamina') {
        return new URL('../assets/img/skills/stamina.png', import.meta.url).href;
      } else if (this.type == 'sight') {
        return new URL('../assets/img/skills/sight.png', import.meta.url).href;
      } else if (this.type == 'accelerate') {
        return new URL('../assets/img/skills/accelerate.png', import.meta.url).href;
      }
      return '';
    }
  }
};
</script>

<style scoped>
.skill-icon {
  display: inline-flex;
  align-items: center;
  padding: 4px 6px;
  background: linear-gradient(to right, #fbfae1, #ffeda5, #ffca4f);
  border-radius: 4px;
}
.skill-icon img {
  width: 22px;
  height: 22px;
}
.skill-name {
  margin-left: 4px;
  color: #855F40;
  font-size: 14px;
}
</style>
