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
                  <select v-model="recoverTP" class="form-control" id="selectAutoRecoverTP">
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
              <div class="col-4">
                <div class="form-group">
                  <label>借用支援卡选择</label>
                  <select v-model="selectedSupportCard" class="form-control" id="selectedSupportCard">
                    <option v-for="card in umausumeSupportCardList" :value="card">({{card.desc}}) {{card.name}}</option>
                  </select>
                </div>
              </div>
              <div class="col-2">
                <div class="form-group">
                  <label for="selectSupportCardLevel">支援卡等级(≥)</label>
                  <input v-model="supportCardLevel" type="number" class="form-control" id="selectSupportCardLevel" placeholder="">
                </div>
              </div>
              <div class="col-3">
                <div class="form-group">
                  <label for="inputClockUseLimit">使用闹钟数量限制</label>
                  <input v-model="clockUseLimit" type="number" class="form-control" id="inputClockUseLimit" placeholder="">
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
                    <textarea type="text" disabled v-model="extraRace" class="form-control" id="race-select"></textarea>
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
                      <input class="form-check-input position-static" v-model="extraRace" type="checkbox" :id="race.id" :value="race.id"><label :for="race.id" v-if="race.type==='GI'||race.type==='GII'&&!this.hideG2||race.type==='GIII'&&!this.hideG3">
                        <span v-if="race.type === 'GIII'">&nbsp;<span style="background-color: #58C471;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>
                        <span v-if="race.type === 'GII'">&nbsp;<span style="background-color: #F75A86;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>
                        <span v-if="race.type === 'GI'">&nbsp;<span style="background-color: #3485E3;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>{{race.date}} {{race.name}}</label>
                    </div>
                  </div>
                </div>
                <div class="col">
                  <div>第二年</div>
                  <br/>
                  <div class="form-check">
                    <div v-for="race in umamusumeRaceList_2">
                      <input class="form-check-input position-static" v-model="extraRace" type="checkbox" :id="race.id" :value="race.id"><label :for="race.id" v-if="race.type==='GI'||race.type==='GII'&&!this.hideG2||race.type==='GIII'&&!this.hideG3">
                        <span v-if="race.type === 'GIII'">&nbsp;<span style="background-color: #58C471;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>
                        <span v-if="race.type === 'GII'">&nbsp;<span style="background-color: #F75A86;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>
                        <span v-if="race.type === 'GI'">&nbsp;<span style="background-color: #3485E3;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>{{race.date}} {{race.name}}</label>
                    </div>
                  </div>
                </div>
                <div class="col">
                  <div>第三年</div>
                  <br/>
                  <div class="form-check">
                    <div v-for="race in umamusumeRaceList_3">
                      <input class="form-check-input position-static" v-model="extraRace" type="checkbox" :id="race.id" :value="race.id"><label :for="race.id" v-if="race.type==='GI'||race.type==='GII'&&!this.hideG2||race.type==='GIII'&&!this.hideG3">
                        <span v-if="race.type === 'GIII'">&nbsp;<span style="background-color: #58C471;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>
                        <span v-if="race.type === 'GII'">&nbsp;<span style="background-color: #F75A86;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>
                        <span v-if="race.type === 'GI'">&nbsp;<span style="background-color: #3485E3;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>{{race.date}} {{race.name}}</label>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="form-group mb-0">
              <div class="row">
                <div class="col">
                  <div class="form-group">
                    <label for="skill-learn">技能学习</label>
                    <textarea type="text"  v-model="skillLearn" class="form-control" id="skill-learn" placeholder="技能1名称,技能2名称,....(使用英文逗号)"></textarea>
                  </div>
                </div>
              </div>
            </div>
            <div class="form-group">
              <div class="row">
                <div class="col-3">
                  <div class="form-group">
                    <label for="learnSkillOnlyUserProvidedSelector">育成中仅允许学习上面的技能</label>
                    <select v-model="learnSkillOnlyUserProvided" class="form-control" id="learnSkillOnlyUserProvidedSelector">
                      <option :value=true>是</option>
                      <option :value=false>否</option>
                    </select>
                  </div>
                </div>
                <div class="col-3">
                  <div class="form-group">
                    <label for="learnSkillBeforeRaceSelector">在参赛前学习技能</label>
                    <select disabled v-model="learnSkillBeforeRace" class="form-control" id="learnSkillBeforeRace">
                      <option :value=true>是</option>
                      <option :value=false>否</option>
                    </select>
                  </div>
                </div>
                <div class="col-3">
                  <div class="form-group">
                    <label for="inputSkillLearnThresholdLimit">育成中pt超过此值后学习技能</label>
                    <input v-model="learnSkillThreshold" type="number" class="form-control" id="inputSkillLearnThresholdLimit" placeholder="">
                  </div>
                </div>
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
      hideG2: false,
      hideG3: false,
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
        {id:1, name:'在耀眼景色的前方', desc:'速铃鹿'},
        {id:2, name:'献上全国第一的演出' , desc: '根特别周'},
        {id:3, name:'有梦想就要大声说出来！', desc: '速帝王'},
        {id:4, name:'不沉舰的进击', desc: '耐黄金船'},
        {id:5, name:'伏特加之路', desc: '力伏特加'},
        {id:6, name:'万紫千红中一枝独秀', desc: '根草上飞'},
        {id:7, name:'热情的冠军', desc: '力神鹰'},
        {id:8, name:'期待已久的计谋', desc: '耐青云'},
        {id:9, name:'划破天空的闪电少女！', desc: '耐玉藻十字'},
        {id:10, name:'全身心的感谢', desc: '智美妙姿势'},
        {id:11, name:'飞奔吧，闪耀吧', desc: '根风神'},
        {id:12, name:'B·N·Winner!', desc: '根奖券'},
        {id:13, name:'冲向前方7厘米之外', desc: '智空中神宫'},
        {id:14, name:'Run(my)way', desc: '速黄金城'},
        {id:15, name:'好快！好吃！好快', desc: '速进王'},
        {id:16, name:'一颗安心糖', desc: '耐小海湾'},
        {id:17, name:'这就是我的优俊偶像之道', desc: '力飞鹰'},
        {id:18, name:'哪怕还未长大', desc: '速西野花'},
        {id:19, name:'必杀技！双胡萝卜拳', desc: '速微光飞驹'},
        {id:20, name:'欢迎来到特雷森学园！', desc: '绿帽'},
        {id:21, name:'夕阳是憧憬之色', desc: '速特别周'},
        {id:22, name:'要受人喜爱啊', desc: '力小栗帽'},
        {id:23, name:'涡轮引擎马力全开！', desc: '速双涡轮'},
        {id:24, name:'心中的烈火无法抑制', desc: '力八重'},
        {id:25, name:'身后迫近的热浪是动力', desc: '速北黑'},
        {id:26, name:'超越那前方的背影', desc: '耐光钻'},
        {id:27, name:'身为新娘！', desc: '速川上公主'},
      ],
      umamusumeRaceList_1:[
        {id:1401, name:'函馆初级锦标赛',date: '7月后', type: 'GIII'},
        {id:1601, name:'新潟初级锦标赛',date: '8月后', type: 'GIII'},
        {id:1701, name:'札幌初级锦标赛',date: '9月前', type: 'GIII'},
        {id:1702, name:'小仓初级锦标赛',date: '9月前', type: 'GIII'},
        {id:1902, name:'沙特阿拉伯皇家杯',date: '10月前', type: 'GIII'},
        {id:2002, name:'阿耳忒米斯锦标赛',date: '10月后', type: 'GIII'},
        {id:2102, name:'京王杯初级锦标赛',date: '11月前', type: 'GII'},
        {id:2103, name:'每日杯初级锦标赛',date: '11月前', type: 'GII'},
        {id:2104, name:'幻想锦标赛',date: '11月前', type: 'GIII'},
        {id:2202, name:'东京体育馆初级锦标赛',date: '11月后', type: 'GIII'},
        {id:2203, name:'京都初级锦标赛',date: '11月后', type: 'GIII'},
        {id:2302, name:'阪神初级少女杯赛', date: '12月前', type: 'GI'},
        {id:2303, name:'朝日杯未来锦标赛', date: '12月前', type: 'GI'},
        {id:2401, name:'希望锦标赛', date: '12月后', type: 'GI'},
      ],
      umamusumeRaceList_2:[
        {id:2501, name:'新山纪念', date: '1月前', type: 'GIII'},
        {id:2502, name:'精灵锦标赛', date: '1月前', type: 'GIII'},
        {id:2503, name:'京成杯', date: '1月前', type: 'GIII'},
        {id:2701, name:'如月奖', date: '2月前', type: 'GIII'},
        {id:2702, name:'女王杯', date: '2月前', type: 'GIII'},
        {id:2703, name:'共同通信杯', date: '2月前', type: 'GIII'},
        {id:2903, name:'弥生奖', date: '3月前', type: 'GII'},
        {id:2904, name:'少女竞技赛', date: '3月前', type: 'GII'},
        {id:2905, name:'郁金香奖', date: '3月前', type: 'GII'},
        {id:3001, name:'百花杯', date: '3月后', type: 'GIII'},
        {id:3003, name:'春季锦标赛', date: '3月后', type: 'GII'},
        {id:3004, name:'游隼锦标赛', date: '3月后', type: 'GIII'},
        {id:3005, name:'每日杯', date: '3月后', type: 'GIII'},
        {id:3103, name:'樱花奖', date: '4月前', type: 'GI'},
        {id:3104, name:'皐月奖', date: '4月前', type: 'GI'},
        {id:3105, name:'新西兰杯', date: '4月前', type: 'GII'},
        {id:3106, name:'阿灵顿杯', date: '4月前', type: 'GIII'},
        {id:3204, name:'芙洛拉锦标赛', date: '4月后', type: 'GII'},
        {id:3205, name:'青叶奖', date: '4月后', type: 'GII'},
        {id:3303, name:'NHK 英里杯', date: '5月前', type: 'GI'},
        {id:3304, name:'京都新闻杯', date: '5月前', type: 'GII'},
        {id:3403, name:'奥克斯', date: '5月后', type: 'GI'},
        {id:3404, name:'日本德比 东京优骏', date: '5月后', type: 'GI'},
        {id:3405, name:'葵锦标赛', date: '5月后', type: 'GIII'},
        {id:3504, name:'东京英里赛', date: '6月前', type: 'GI'},
        {id:3506, name:'叶森杯', date: '6月前', type: 'GIII'},
        {id:3505, name:'鸣尾纪念', date: '6月前', type: 'GIII'},
        {id:3501, name:'人鱼锦标赛', date: '6月前', type: 'GIII'},
        {id:3608, name:'函馆短途锦标赛', date: '6月后', type: 'GIII'},
        {id:3601, name:'独角兽锦标赛', date: '6月后', type: 'GIII'},
        {id:3607, name:'宝塚纪念', date: '6月后', type: 'GI'},
        {id:3708, name:'函馆纪念', date: '7月前', type: 'GIII'},
        {id:3706, name:'CBC奖', date: '7月前', type: 'GIII'},
        {id:3707, name:'七夕奖', date: '7月前', type: 'GIII'},
        {id:3709, name:'广播NIKKEI奖', date: '7月前', type: 'GIII'},
        {id:3705, name:'日本泥地德比', date: '7月前', type: 'GI'},
        {id:4101, name:'人马锦标赛', date: '9月前', type: 'GII'},
        {id:4102, name:'玫瑰锦标赛', date: '9月前', type: 'GII'},
        {id:4103, name:'新潟記念', date: '9月前', type: 'GIII'},
        {id:4104, name:'京成杯秋季让磅赛', date: '9月前', type: 'GIII'},
        {id:4105, name:'紫苑锦标赛', date: '9月前', type: 'GIII'},
        {id:4201, name:'短途者锦标赛', date: '9月后', type: 'GI'},
        {id:4202, name:'神户新闻杯', date: '9月后', type: 'GII'},
        {id:4203, name:'全国邀请赛', date: '9月后', type: 'GII'},
        {id:4204, name:'圣光纪念', date: '9月后', type: 'GII'},
        {id:4205, name:'天狼星锦标赛', date: '9月后', type: 'GIII'},
        {id:4301, name:'每日王冠', date: '10月前', type: 'GII'},
        {id:4302, name:'京都大奖赛', date: '10月前', type: 'GII'},
        {id:4303, name:'府中优俊少女锦标赛', date: '10月前', type: 'GIII'},
        {id:4401, name:'天鹅锦标赛', date: '10月后', type: 'GII'},
        {id:4402, name:'富士锦标赛', date: '10月后', type: 'GII'},
        {id:4407, name:'天王奖(秋)', date: '10月后', type: 'GI'},
        {id:4408, name:'秋华奖', date: '10月后', type: 'GI'},
        {id:4409, name:'菊花奖', date: '10月后', type: 'GI'},
        {id:4506, name:'伊丽莎白女王杯', date: '11月前', type: 'GI'},
        {id:4507, name:'JBC女士经典赛', date: '11月前', type: 'GI'},
        {id:4508, name:'JBC短途赛', date: '11月前', type: 'GI'},
        {id:4509, name:'JBC经典赛', date: '11月前', type: 'GI'},
        {id:4601, name:'京阪杯', date: '11月后', type: 'GIII'},
        {id:4607, name:'英里冠军杯', date: '11月后', type: 'GI'},
        {id:4608, name:'日本杯', date: '11月后', type: 'GI'},
        {id:4701, name:'长途锦标赛', date: '12月前', type: 'GII'},
        {id:4702, name:'挑战杯', date: '12月前', type: 'GIII'},
        {id:4705, name:'绿松石锦标赛', date: '12月前', type: 'GIII'},
        {id:4705, name:'中日新闻杯', date: '12月前', type: 'GIII'},
        {id:4711, name:'日本冠军杯', date: '12月前', type: 'GI'},
        {id:4804, name:'中山大奖赛', date: '12月后', type: 'GI'},
        {id:4805, name:'东京大奖赛', date: '12月后', type: 'GI'},
      ],
      umamusumeRaceList_3:[
        {id:4901, name:'日经新春杯', date: '1月前', type: 'GII'},
        {id:4902, name:'京都金杯', date: '1月前', type: 'GIII'},
        {id:4903, name:'中山金杯', date: '1月前', type: 'GIII'},
        {id:4904, name:'爱知杯', date: '1月前', type: 'GIII'},
        {id:5001, name:'东海锦标赛', date: '1月后', type: 'GII'},
        {id:5002, name:'美国JCC', date: '1月后', type: 'GII'},
        {id:5003, name:'丝绸之路锦标赛', date: '1月后', type: 'GIII'},
        {id:5004, name:'根岸锦标赛', date: '1月后', type: 'GIII'},
        {id:5101, name:'京都纪念', date: '2月前', type: 'GII'},
        {id:5102, name:'东京新闻杯', date: '2月前', type: 'GIII'},
        {id:5201, name:'中山纪念', date: '2月后', type: 'GII'},
        {id:5202, name:'京都优骏少女锦标赛', date: '2月后', type: 'GIII'},
        {id:5203, name:'钻石锦标赛', date: '2月后', type: 'GIII'},
        {id:5204, name:'小仓大奖赛', date: '2月后', type: 'GIII'},
        {id:5208, name:'二月锦标赛', date: '2月后', type: 'GI'},
        {id:5301, name:'金鯱賞', date: '3月前', type: 'GII'},
        {id:5302, name:'海洋锦标赛', date: '3月前', type: 'GIII'},
        {id:5303, name:'中山优俊少女锦标赛', date: '3月前', type: 'GIII'},
        {id:5403, name:'三月锦标赛', date: '3月后', type: 'GIII'},
        {id:5406, name:'中京短途赛', date: '3月后', type: 'GI'},
        {id:5407, name:'大阪杯', date: '3月后', type: 'GI'},
        {id:5501, name:'阪神优俊少女锦标赛', date: '4月前', type: 'GII'},
        {id:5503, name:'心宿二锦标赛', date: '4月前', type: 'GIII'},
        {id:5601, name:'英里杯', date: '4月后', type: 'GII'},
        {id:5605, name:'天王奖(春)', date: '4月后', type: 'GI'},
        {id:5701, name:'京王杯春季杯', date: '5月前', type: 'GII'},
        {id:5702, name:'新潟大奖赛', date: '5月前', type: 'GIII'},
        {id:5709, name:'维多利亚英里杯', date: '5月前', type: 'GI'},
        {id:5801, name:'目黑記念', date: '5月后', type: 'GII'},
        {id:5802, name:'平安锦标赛', date: '5月后', type: 'GIII'},
        {id:5904, name:'东京英里赛', date: '6月前', type: 'GI'},
        {id:5905, name:'鳴尾記念', date: '6月前', type: 'GIII'},
        {id:6006, name:'宝塚記念', date: '6月后', type: 'GI'},
        {id:6007, name:'函館短途锦标赛', date: '6月后', type: 'GIII'},
        {id:6008, name:'帝王奖', date: '6月后', type: 'GI'},
        {id:6501, name:'人马锦标赛', date: '9月前', type: 'GII'},
        {id:6502, name:'新潟記念', date: '9月前', type: 'GIII'},
        {id:6503, name:'京成杯秋季让磅赛', date: '9月前', type: 'GIII'},
        {id:6603, name:'天狼星锦标赛', date: '9月后', type: 'GIII'},
        {id:6602, name:'全国邀请赛', date: '9月后', type: 'GII'},
        {id:6601, name:'短途者锦标赛', date: '9月后', type: 'GI'},
        {id:6701, name:'每日王冠', date: '10月前', type: 'GII'},
        {id:6702, name:'京都大奖赛', date: '10月前', type: 'GII'},
        {id:6801, name:'天鹅锦标赛', date: '10月后', type: 'GII'},
        {id:6802, name:'富士锦标赛', date: '10月后', type: 'GII'},
        {id:6807, name:'天王奖(秋)', date: '10月后', type: 'GI'},
        {id:6901, name:'阿根廷杯', date: '11月前', type: 'GII'},
        {id:6906, name:'伊丽莎白女王杯', date: '11月前', type: 'GI'},
        {id:6907, name:'JBC女士经典赛', date: '11月前', type: 'GI'},
        {id:6908, name:'JBC短途赛', date: '11月前', type: 'GI'},
        {id:6909, name:'JBC经典赛', date: '11月前', type: 'GI'},
        {id:7001, name:'京阪杯', date: '11月后', type: 'GIII'},
        {id:7007, name:'英里冠军杯', date: '11月后', type: 'GI'},
        {id:7008, name:'日本杯', date: '11月后', type: 'GI'},
        {id:7101, name:'长途锦标赛', date: '12月前', type: 'GII'},
        {id:7103, name:'中日新闻杯', date: '12月前', type: 'GIII'},
        {id:7111, name:'日本冠军杯', date: '12月前', type: 'GI'},
        {id:7201, name:'阪神杯', date: '12月后', type: 'GII'},
        {id:7204, name:'中山大奖赛', date: '12月后', type: 'GI'},
        {id:7205, name:'东京大奖赛', date: '12月后', type: 'GI'}],
      cultivatePresets:[],
      cultivateDefaultPresets:[
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
          expect_attribute:[800, 650, 800, 300, 400],
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
          expect_attribute:[800, 600, 600, 300, 400],
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
          expect_attribute:[700, 700, 600, 350, 400],
          follow_support_card: {id:16, name:'一颗安心糖'},
          follow_support_card_level: 50,
          clock_use_limit: 99,
          learn_skill_threshold: 9999,
          race_tactic_1: 4,
          race_tactic_2: 4,
          race_tactic_3: 4,
        },
        {
          name:"历战小栗帽35战60w粉丝(需求觉醒3,借满破小海湾,种马速耐,支援卡带赛后加成高的)",
          race_list:[1601,1701,1902,2103,2302,2401,2701,2905,3103,3303,3404,3601,4102,4203,4408,4506,4607,4804,4902,5208,5407,5601,5709,5904,6006,6602,6701,6807,7007,7111,7204],
          skill:"大胃王",
          expect_attribute:[700,500,700,350,350],
          follow_support_card:{"id":16,"name":"一颗安心糖","desc":"耐小海湾"},
          follow_support_card_level:50,
          clock_use_limit:2,
          learn_skill_threshold:450,
          race_tactic_1:4,
          race_tactic_2:3,
          race_tactic_3:3
        }
      ],
      expectSpeedValue : 650,
      expectStaminaValue : 600,
      expectPowerValue: 650,
      expectWillValue: 300,
      expectIntelligenceValue:300,

      supportCardLevel: 50,
      
      presetsUse: {
          name: "默认",
          race_list: [],
          skill: "",
          expect_attribute:[650, 800, 650, 400, 400],
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
      learnSkillOnlyUserProvided: false,
      learnSkillBeforeRace: false,
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
          "allow_recover_tp": this.recoverTP,
          "learn_skill_only_user_provided": this.learnSkillOnlyUserProvided
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
          let tmplist = []
          tmplist = tmplist.concat(this.cultivateDefaultPresets)
          tmplist = tmplist.concat(res.data)
          this.cultivatePresets = tmplist
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
          this.getPresets()
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