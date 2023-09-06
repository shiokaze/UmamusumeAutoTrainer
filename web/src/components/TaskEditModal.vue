<template>
  <div id="create-task-list-modal" class="modal fade">
    <div  class="modal-dialog modal-dialog-centered modal-xl">
      <div class="modal-content">
        <h5 class="modal-header">
          新建任务
        </h5>
        <div class="modal-body">
          <form>
            <div class="form-group">
              <label for="selectTaskType">任务选择</label>
              <select v-model="selectedUmamusumeTaskType" class="form-control" id="selectTaskType">
                <option v-for="task in umamusumeTaskTypeList" :value="task">{{task.name}}</option>
              </select>
            </div>
            <div class="form-group">
              <label for="selectExecuteMode">执行模式选择</label>
              <select v-model="selectedExecuteMode" class="form-control" id="selectExecuteMode">
                <option value=1>一次性</option>
              </select>
            </div>
            <div class="row">
              <div class="col">
                <div class="form-group">
                  <label for="selectSernaio">剧本选择</label>
                  <select class="form-control" id="selectSernaio">
                    <option value=1>URA</option>
                  </select>
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="selectUmamusume">赛马娘选择</label>
                  <select disabled class="form-control" id="selectUmamusume">
                    <option value=1>使用上次选择</option>
                  </select>
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="selectAutoRecoverTP">TP不足时自动恢复（仅使用药水）</label>
                  <select disabled v-model="recoverTP" class="form-control" id="selectAutoRecoverTP">
                    <option :value=true>是</option>
                    <option :value=false>否</option>
                  </select>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-8">
                <div class="form-group">
                  <label for="race-select">使用预设</label>
                    <div class="form-inline">
                      <select v-model="presetsUse" style="text-overflow: ellipsis;width: 40em;"  class="form-control" id="use_presets">
                        <option v-for="set in cultivatePresets" :value="set">{{set.name}}</option>
                      </select>
                      <span class="btn auto-btn ml-2" v-on:click="applyPresetRace">应用</span>
                    </div>
                </div>
              </div>
              <div class="col-4">
                <div class="form-group">
                  <label for="presetNameEditInput">保存为预设</label>
                  <div class="form-inline">
                    <input v-model="presetNameEdit" type="text" class="form-control" id="presetNameEditInput" placeholder="预设名称">
                    <span class="btn auto-btn ml-2" v-on:click="addPresets">保存</span>
                  </div>
                </div>
              </div>
            </div>
            
            <div class="row">
              <div class="col">
                <div class="form-group">
                  <label>借用支援卡选择</label>
                  <select v-model="selectedSupportCard" class="form-control" id="selectedSupportCard">
                    <option v-for="card in umausumeSupportCardList" :value="card">{{card.name}}</option>
                  </select>
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="selectSupportCardLevel">支援卡等级(大于或等于)</label>
                  <input v-model="supportCardLevel" type="number" class="form-control" id="selectSupportCardLevel" placeholder="">
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="inputClockUseLimit">使用闹钟数量限制</label>
                  <input v-model="clockUseLimit" type="number" class="form-control" id="inputClockUseLimit" placeholder="">
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="inputSkillLearnThresholdLimit">育成中pt超过此值后学习技能</label>
                  <input v-model="learnSkillThreshold" type="number" class="form-control" id="inputSkillLearnThresholdLimit" placeholder="">
                </div>
              </div>
            </div>
            <div class="form-group">
              <div>目标属性</div>
            </div>
            <div class="row">
              <div class="col">
                <div class="form-group">
                    <label for="speed-value-input">速度</label>
                    <input type="number" v-model="expectSpeedValue" class="form-control" id="speed-value-input">
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="stamina-value-input">耐力</label>
                  <input type="number" v-model="expectStaminaValue" class="form-control" id="stamina-value-input">
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="power-value-input">力量</label>
                  <input type="number" v-model="expectPowerValue" class="form-control" id="power-value-input">
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="will-value-input">毅力</label>
                  <input type="number" v-model="expectWillValue" class="form-control" id="will-value-input">
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="intelligence-value-input">智力</label>
                  <input type="number" v-model="expectIntelligenceValue" class="form-control" id="intelligence-value-input">
                </div>
              </div>
            </div>
            <div class="form-group">
              <div>跑法选择</div>
            </div>
            <div class="row">
              <div class="col">
                <div class="form-group">
                  <label for="selectTactic1">第一年</label>
                  <select v-model="selectedRaceTactic1" class="form-control" id="selectTactic1">
                    <option :value=1>后追（追）</option>
                    <option :value=2>居中（差）</option>
                    <option :value=3>前列（先）</option>
                    <option :value=4>领头（逃）</option>
                  </select>
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="selectTactic2">第二年</label>
                  <select v-model="selectedRaceTactic2" class="form-control" id="selectTactic2">
                    <option :value=1>后追（追）</option>
                    <option :value=2>居中（差）</option>
                    <option :value=3>前列（先）</option>
                    <option :value=4>领头（逃）</option>
                  </select>
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="selectTactic3">第三年</label>
                  <select v-model="selectedRaceTactic3" class="form-control" id="selectTactic3">
                    <option :value=1>后追（追）</option>
                    <option :value=2>居中（差）</option>
                    <option :value=3>前列（先）</option>
                    <option :value=4>领头（逃）</option>
                  </select>
                </div>
              </div>
            </div>
            <div class="form-group">
              <div class="row">
                <div class="col">
                  <div class="form-group">
                    <label for="race-select">额外赛程选择</label>
                    <input type="text" disabled v-model="extraRace" class="form-control" id="race-select">
                  </div>
                </div>
              </div>
              <div class="form-group">
              <span v-if="!showRaceList" class="btn auto-btn" style="width: 100%; background-color:#6c757d;" v-on:click="switchRaceList">展开赛程选项</span>
              <span v-if="showRaceList" class="btn auto-btn" style="width: 100%; background-color:#6c757d;" v-on:click="switchRaceList">收起赛程选项</span>
              </div>
              <div class="row" v-if="showRaceList"> 
                <div class="col">
                  <div>第一年</div>
                  <br/>
                  <div class="form-check">
                    <div v-for="race in umamusumeRaceList_1">
                      <input class="form-check-input position-static" v-model="extraRace" type="checkbox" :id="race.id" :value="race.id"><label :for="race.id">{{race.date}} {{race.name}}</label>
                    </div>
                  </div>
                </div>
                <div class="col">
                  <div>第二年</div>
                  <br/>
                  <div class="form-check">
                    <div v-for="race in umamusumeRaceList_2">
                      <input class="form-check-input position-static" v-model="extraRace" type="checkbox" :id="race.id" :value="race.id"><label :for="race.id">{{race.date}} {{race.name}}</label>
                    </div>
                  </div>
                </div>
                <div class="col">
                  <div>第三年</div>
                  <br/>
                  <div class="form-check">
                    <div v-for="race in umamusumeRaceList_3">
                      <input class="form-check-input position-static" v-model="extraRace" type="checkbox" :id="race.id" :value="race.id"><label :for="race.id">{{race.date}} {{race.name}}</label>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="form-group">
              <div class="form-group">
                <label for="skill-learn">技能学习</label>
                <input type="text"  v-model="skillLearn" class="form-control" id="skill-learn" placeholder="技能1名称,技能2名称,....(使用英文逗号)">
              </div>
            </div>
          </form>
          <!-- <div class="part">
            <br>
            <h6>定时设置</h6>
            <hr />
            <div class="row">
              <label for="cronInput" class="col-2 col-form-label">cron表达式</label>
              <div class="col-10">
                <input v-model="cron"  class="form-control" id="cronInput">
              </div>
            </div>
          </div> -->
        </div>
        <div class="modal-footer">
          <span class="btn auto-btn" v-on:click="addTask">确定</span>
        </div>
      </div>
      <!-- 通知 -->
      <div class="position-fixed" style="z-index: 5; right: 40%; width: 300px;">
        <div id="liveToast" class="toast hide" role="alert" aria-live="assertive" aria-atomic="true" data-delay="2000">
          <div class="toast-body">
            ✔ 预设保存成功
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TaskEditModal",
  data:function () {
    return{
      showRaceList:false,
      dataReady:false,
      levelDataList:[],
      umamusumeTaskTypeList:[
        {
          id: 1,
          name: "育成",
        }
      ],
      umamusumeList:[
        {id:1, name:'特别周'},
        {id:2, name:'无声铃鹿'},
        {id:3, name:'东海帝王'},
        {id:4, name:'丸善斯基'},
        {id:5, name:'小栗帽'},
        {id:6, name:'大树快车'},
        {id:7, name:'目白麦昆'},
        {id:8, name:'好歌剧'},
        {id:9, name:'鲁道夫象征'},
        {id:10, name:'米浴'},
        {id:11, name:'黄金船'},
        {id:12, name:'伏特加'},
        {id:13, name:'大和赤骥'},
        {id:14, name:'草上飞'},
        {id:15, name:'神鹰'},
        {id:16, name:'气槽'},
        {id:17, name:'重炮'},
        {id:18, name:'超级小海湾'},
        {id:19, name:'目白赖恩'},
        {id:20, name:'爱丽速子'},
        {id:21, name:'胜利奖券'},
        {id:22, name:'樱花进王'},
        {id:23, name:'春乌拉拉'},
        {id:24, name:'待兼福来'},
        {id:25, name:'优秀素质'},
        {id:26, name:'帝王光环'},
      ],
      umausumeSupportCardList:[
        {id:1, name:'在耀眼景色的前方'},
        {id:2, name:'献上全国第一的演出'},
        {id:3, name:'有梦想就要大声说出来！'},
        {id:4, name:'不沉舰的进击'},
        {id:5, name:'伏特加之路'},
        {id:6, name:'万紫千红中一枝独秀'},
        {id:7, name:'热情的冠军'},
        {id:8, name:'期待已久的计谋'},
        {id:9, name:'划破天空的闪电少女！'},
        {id:10, name:'全身心的感谢'},
        {id:11, name:'飞奔吧，闪耀吧'},
        {id:12, name:'B·N·Winner!'},
        {id:13, name:'冲向前方7厘米之外'},
        {id:14, name:'Run(my)way'},
        {id:15, name:'好快！好吃！好快'},
        {id:16, name:'一颗安心糖'},
        {id:17, name:'这就是我的优俊偶像之道'},
        {id:18, name:'哪怕还未长大'},
        {id:19, name:'必杀技！双胡萝卜拳'},
        {id:20, name:'欢迎来到特雷森学园！'},
      ],
      umamusumeRaceList_1:[
        {id:1401, name:'函馆初级锦标赛',date: '7月后', type: 'g3'},
        {id:1601, name:'新潟初级锦标赛',date: '8月后', type: 'g3'},
        {id:1701, name:'札幌初级锦标赛',date: '9月前', type: 'g3'},
        {id:1702, name:'小仓初级锦标赛',date: '9月前', type: 'g3'},
        {id:1902, name:'沙特阿拉伯皇家杯',date: '10月前', type: 'g3'},
        {id:2002, name:'阿耳忒米斯锦标赛',date: '10月后', type: 'g3'},
        {id:2102, name:'京王杯初级锦标赛',date: '11月前', type: 'g2'},
        {id:2103, name:'每日杯初级锦标赛',date: '11月前', type: 'g2'},
        {id:2104, name:'幻想锦标赛',date: '11月前', type: 'g3'},
        {id:2202, name:'东京体育馆初级锦标赛',date: '11月后', type: 'g3'},
        {id:2203, name:'京都初级锦标赛',date: '11月后', type: 'g3'},
        {id:2302, name:'阪神初级少女杯赛', date: '12月前', type: 'g1'},
        {id:2303, name:'朝日杯未来锦标赛', date: '12月前', type: 'g1'},
        {id:2401, name:'希望锦标赛', date: '12月前', type: 'g1'},
      ],
      umamusumeRaceList_2:[
        {id:3103, name:'樱花奖', date: '4月前', type: 'g1'},
        {id:3104, name:'皐月奖', date: '4月前', type: 'g1'},
        {id:3303, name:'NHK 英里杯', date: '5月前', type: 'g1'},
        {id:3403, name:'奥克斯', date: '5月后', type: 'g1'},
        {id:3404, name:'日本德比 东京优骏', date: '5月后', type: 'g1'},
        {id:3504, name:'东京英里赛', date: '6月前', type: 'g1'},
        {id:3607, name:'宝塚纪念', date: '6月后', type: 'g1'},
        {id:3705, name:'日本泥地德比', date: '7月前', type: 'g1'},
        {id:4201, name:'短途者锦标赛', date: '9月后', type: 'g1'},
        {id:4407, name:'天王奖(秋)', date: '10月后', type: 'g1'},
        {id:4408, name:'秋华奖', date: '10月后', type: 'g1'},
        {id:4409, name:'菊花奖', date: '10月后', type: 'g1'},
        {id:4506, name:'伊丽莎白女王杯', date: '11月前', type: 'g1'},
        {id:4507, name:'JBC女士经典赛', date: '11月前', type: 'g1'},
        {id:4508, name:'JBC短途赛', date: '11月前', type: 'g1'},
        {id:4509, name:'JBC经典赛', date: '11月前', type: 'g1'},
        {id:4607, name:'英里冠军杯', date: '11月后', type: 'g1'},
        {id:4608, name:'日本杯', date: '11月后', type: 'g1'},
        {id:4711, name:'日本冠军杯', date: '12月前', type: 'g1'},
        {id:4804, name:'中山大奖赛', date: '12月后', type: 'g1'},
        {id:4805, name:'东京大奖赛', date: '12月后', type: 'g1'},
      ],
      umamusumeRaceList_3:[
        {id:5208, name:'二月锦标赛', date: '2月后', type: 'g1'},
        {id:5406, name:'中京短途赛', date: '3月后', type: 'g1'},
        {id:5407, name:'大阪杯', date: '3月后', type: 'g1'},
        {id:5605, name:'天王奖(春)', date: '4月后', type: 'g1'},
        {id:5709, name:'维多利亚英里杯', date: '5月前', type: 'g1'},
        {id:5904, name:'东京英里赛', date: '6月前', type: 'g1'},
        {id:6006, name:'宝塚記念', date: '6月后', type: 'g1'},
        {id:6008, name:'帝王奖', date: '6月后', type: 'g1'},
        {id:6601, name:'短途者锦标赛', date: '9月后', type: 'g1'},
        {id:6807, name:'天王奖(秋)', date: '10月后', type: 'g1'},
        {id:6906, name:'伊丽莎白女王杯', date: '11月前', type: 'g1'},
        {id:6907, name:'JBC女士经典赛', date: '11月前', type: 'g1'},
        {id:6908, name:'JBC短途赛', date: '11月前', type: 'g1'},
        {id:6909, name:'JBC经典赛', date: '11月前', type: 'g1'},
        {id:7007, name:'英里冠军杯', date: '11月后', type: 'g1'},
        {id:7008, name:'日本杯', date: '11月后', type: 'g1'},
        {id:7111, name:'日本冠军杯', date: '12月前', type: 'g1'},
        {id:7204, name:'中山大奖赛', date: '12月后', type: 'g1'},
        {id:7205, name:'东京大奖赛', date: '12月后', type: 'g1'}],
      cultivatePresets:[
      {
          name: "默认",
          race_list: [],
          skill: "",
          expect_attribute:[800, 800, 800, 400, 400],
          follow_support_card: {id:1, name:'在耀眼景色的前方'},
          follow_support_card_level: 50,
          clock_use_limit: 99,
          learn_skill_threshold: 9999,
          race_tactic_1: 4,
          race_tactic_2: 4,
          race_tactic_3: 4,

        },
        {
          name: "小栗帽基础育成赛程",
          race_list: [1701, 2303, 2401, 5208, 5407, 5904],
          skill: "",
          expect_attribute:[900, 750, 850, 300, 400],
          follow_support_card: {id:16, name:'一颗安心糖'},
          follow_support_card_level: 50,
          clock_use_limit: 99,
          learn_skill_threshold: 9999,
          race_tactic_1: 4,
          race_tactic_2: 4,
          race_tactic_3: 4,
        },
        {
          name: "大和赤骥基础育成赛程",
          race_list: [1701, 2303],
          skill: "",
          expect_attribute:[900, 800, 800, 300, 400],
          follow_support_card: {id:16, name:'一颗安心糖'},
          follow_support_card_level: 50,
          clock_use_limit: 99,
          learn_skill_threshold: 9999,
          race_tactic_1: 4,
          race_tactic_2: 4,
          race_tactic_3: 4,
        },
        {
          name: "目白麦昆基础育成赛程",
          race_list: [2203, 2401],
          skill: "",
          expect_attribute:[900, 800, 600, 400, 400],
          follow_support_card: {id:16, name:'一颗安心糖'},
          follow_support_card_level: 50,
          clock_use_limit: 99,
          learn_skill_threshold: 9999,
          race_tactic_1: 4,
          race_tactic_2: 4,
          race_tactic_3: 4,
        }
      ],
      expectSpeedValue : 800,
      expectStaminaValue : 800,
      expectPowerValue: 800,
      expectWillValue: 400,
      expectIntelligenceValue:400,

      supportCardLevel: 50,
      
      presetsUse: {
          name: "默认",
          race_list: [],
          skill: "",
          expect_attribute:[800, 800, 800, 400, 400],
          follow_support_card: {id:1, name:'在耀眼景色的前方'},
          follow_support_card_level: 50,
          clock_use_limit: 99,
          learn_skill_threshold: 9999,
          race_tactic_1: 4,
          race_tactic_2: 4,
          race_tactic_3: 4,
        },
      // ===  已选择  ===
      selectedExecuteMode: 1,
      expectTimes: 0,
      cron: "* * * * *",

      selectedUmamusumeTaskType: undefined,
      selectedSupportCard: undefined,
      extraRace: [],
      skillLearn: "",
      selectedRaceTactic1: 4,
      selectedRaceTactic2: 4,
      selectedRaceTactic3: 4,
      clockUseLimit: 99,
      learnSkillThreshold: 9999,
      recoverTP: false,
      presetNameEdit: "",
      successToast: undefined,
    }
  },
  mounted() {
    this.initSelect()
    this.getPresets()
    this.successToast = $('.toast').toast({})
  },
  methods:{
    initSelect: function (){
      this.selectedSupportCard = this.umausumeSupportCardList[0]
      this.selectedUmamusumeTaskType = this.umamusumeTaskTypeList[0]
    },
    switchRaceList: function(){
      this.showRaceList = !this.showRaceList
    },
    addTask: function (){
      var learn_skill_list = this.skillLearn ? this.skillLearn.split(",") : []
      let payload = {
        app_name: "umamusume",
        task_execute_mode: this.selectedExecuteMode,
        task_type: this.selectedUmamusumeTaskType.id,
        task_desc: this.selectedUmamusumeTaskType.name,
        attachment_data: {
          "expect_attribute": [this.expectSpeedValue, this.expectStaminaValue, this.expectPowerValue, this.expectWillValue, this.expectIntelligenceValue],
          "follow_support_card_name": this.selectedSupportCard.name,
          "follow_support_card_level": this.supportCardLevel,
          "extra_race_list": this.extraRace,
          "learn_skill_list": learn_skill_list,
          "tactic_list": [this.selectedRaceTactic1, this.selectedRaceTactic2, this.selectedRaceTactic3],
          "clock_use_limit": this.clockUseLimit,
          "learn_skill_threshold": this.learnSkillThreshold,
          "recover_tp": this.recoverTP
        },
        cron_job_info:{},
      }
      if(this.selectedExecuteMode === 2){
        payload.cron_job_info = {
          cron: this.cron
        }
      }
      console.log(JSON.stringify(payload))
      this.axios.post("/task", JSON.stringify(payload)).then(
          ()=>{
            $('#create-task-list-modal').modal('hide');
          }
      )
    },
    applyPresetRace: function(){
      this.extraRace = this.presetsUse.race_list
      this.expectSpeedValue = this.presetsUse.expect_attribute[0]
      this.expectStaminaValue = this.presetsUse.expect_attribute[1]
      this.expectPowerValue = this.presetsUse.expect_attribute[2]
      this.expectWillValue = this.presetsUse.expect_attribute[3]
      this.expectIntelligenceValue = this.presetsUse.expect_attribute[4]
      this.selectedSupportCard = this.presetsUse.follow_support_card,
      this.supportCardLevel = this.presetsUse.follow_support_card_level,
      this.clockUseLimit = this.presetsUse.clock_use_limit,
      this.learnSkillThreshold = this.presetsUse.learn_skill_threshold,
      this.selectedRaceTactic1 = this.presetsUse.race_tactic_1,
      this.selectedRaceTactic2 = this.presetsUse.race_tactic_2,
      this.selectedRaceTactic3 = this.presetsUse.race_tactic_3
      this.skillLearn = this.presetsUse.skill
    },
    getPresets: function(){
      this.axios.post("/umamusume/get-presets", "").then(
          res=>{
          this.cultivatePresets = this.cultivatePresets.concat(res.data);
        }
      )
    },
    addPresets: function(){
      let preset = {
        name: this.presetNameEdit,
        race_list: this.extraRace,
        skill: this.skillLearn,
        expect_attribute:[this.expectSpeedValue, this.expectStaminaValue, this.expectPowerValue, this.expectWillValue, this.expectIntelligenceValue],
        follow_support_card: this.selectedSupportCard,
        follow_support_card_level: this.supportCardLevel,
        clock_use_limit: this.clockUseLimit,
        learn_skill_threshold: this.learnSkillThreshold,
        race_tactic_1: this.selectedRaceTactic1,
        race_tactic_2: this.selectedRaceTactic2,
        race_tactic_3: this.selectedRaceTactic3,
      }
      let payload = {
        "preset": JSON.stringify(preset)
      }
      console.log(JSON.stringify(payload))
      this.axios.post("/umamusume/add-presets", JSON.stringify(payload)).then(
        ()=>{
          this.successToast.toast('show')
        } 
      )
    }
  },
  watch:{

  }
}
</script>

<style scoped>

.btn{
  padding: 0.4rem 0.8rem !important;
  font-size: 1rem !important;
}

</style>