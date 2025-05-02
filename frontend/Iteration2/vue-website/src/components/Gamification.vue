<template>
  <div id="game-container">
    <div id="sidebar">
      <div id="step1">
        <div class="step-title">Step 1: Choose Soil</div>
        <div class="options">
          <button @click="handleSoil('Shrubland Clay')">Shrubland Clay</button>
          <button @click="handleSoil('Grassland Loam')">Grassland Loam</button>
          <button @click="handleSoil('Mallee Loam')">Mallee Loam</button>
        </div>
      </div>
      <div id="step2">
        <div class="step-title">Step 2: Ground Cover</div>
        <div class="options">
          <button @click="handleGrass('Heath Hummock')">Heath Hummock</button>
          <button @click="handleGrass('Meadow Tussock')">Meadow Tussock</button>
          <button @click="handleGrass('Spinifex Grass')">Spinifex Grass</button>
        </div>
      </div>
      <div id="step3">
        <div class="step-title">Step 3: Shrubs</div>
        <div class="options">
          <button @click="handleShrub('Mallee Shrub')">Mallee Shrub</button>
          <button @click="handleShrub('Coastal Heath Bush')">Coastal Heath Bush</button>
        </div>
      </div>
      <div id="step4">
        <div class="step-title">Step 4: Trees</div>
        <div class="options">
          <button @click="handleTree('Eucalypt Mallee')">Eucalypt Mallee</button>
          <button @click="handleTree('River Red Gum')">River Red Gum</button>
        </div>
      </div>
      <button id="surprise-btn" @click="showSurprise">Click here for a surprise!</button>
    </div>
    <div id="garden" ref="garden" :style="gardenStyle">
      <img v-for="(shrub, index) in shrubs" :key="'shrub-'+index" 
        :src="shrub.src" class="shrub-item" :style="shrub.style">
      <img v-for="(tree, index) in trees" :key="'tree-'+index" 
        :src="tree.src" class="tree-item" :style="tree.style">
      <transition-group name="fade">
        <div v-for="(animal, index) in animals" :key="animal.name" class="animal-card" :style="animal.style">
          <img :src="animal.img">
          <h4>{{ animal.name }}</h4>
          <small>{{ animal.facts[0] }}</small>
          <button @click="showSpeciesDetail(animal)">Learn more!</button>
        </div>
      </transition-group>
      <img v-if="showingIcon" :src="currentIcon.src" class="anim-icon" :style="currentIcon.style">
    </div>
  </div>

  <!-- 对话框组件 -->
  <div id="feedbackDialog" class="dialog-overlay" :class="{ show: dialogs.feedback.show }">
    <div class="dialog"><p>{{ dialogs.feedback.text }}</p></div>
  </div>
  <div id="nextDialog" class="dialog-overlay" :class="{ show: dialogs.next.show }">
    <div class="dialog"><p>{{ dialogs.next.text }}</p></div>
  </div>
  <div id="congratsDialog" class="dialog-overlay" :class="{ show: dialogs.congrats.show }">
    <div class="dialog"><p>🎉 Congratulations—you saved an animal! 🎉</p></div>
  </div>
  <div id="suggestionModal" class="dialog-overlay" :class="{ show: dialogs.suggestion.show }">
    <div class="dialog">
      <p>{{ dialogs.suggestion.text }}</p>
      <button @click="confirmSuggestion">Yes</button>
      <button @click="cancelSuggestion">No</button>
    </div>
  </div>
  <div id="speciesModal" class="dialog-overlay" :class="{ show: dialogs.species.show }">
    <div class="dialog">
      <img :src="selectedSpecies.img" alt="">
      <h3>{{ selectedSpecies.name }}</h3>
      <p v-html="selectedSpeciesDetail"></p>
      <button @click="closeSpeciesModal">Okay!</button>
    </div>
  </div>

  <canvas id="confetti-canvas" ref="confettiCanvas"></canvas>
</template>

<script>
export default {
  name: 'Gamification',
  data() {
    return {
      selections: {},
      soilColors: {
        'Shrubland Clay': '#d2b48c',
        'Grassland Loam': '#cdb79e',
        'Mallee Loam': '#deb887'
      },
      grassImg: 'https://png.pngtree.com/png-vector/20200917/ourmid/pngtree-green-grass-border-on-transparent-background-vector-png-image_2347202.jpg',
      shrubImgs: {
        'Mallee Shrub': 'https://img.freepik.com/free-psd/lush-green-shrubbery-3d-render-vibrant-foliage_191095-91261.jpg?semt=ais_hybrid&w=740',
        'Coastal Heath Bush': 'https://icon2.cleanpng.com/20240307/hpp/transparent-bushes-bush-green-leaves-white-flowers-grass-single-bush-with-green-leaves-and-white-1710848009966.webp'
      },
      treeImgs: {
        'Eucalypt Mallee': 'https://img.freepik.com/free-psd/majestic-pine-tree-symbol-resilience-longevity_632498-24302.jpg',
        'River Red Gum': 'https://i0.wp.com/www.australiangeographic.com.au/wp-content/uploads/2021/02/H83TRA-scaled.jpg?fit=2560%2C1707&ssl=1'
      },
      species: [
        {
          name: 'Black-eared Miner',
          habitat: { soil: 'Shrubland Clay', grass: 'Heath Hummock', shrub: 'Mallee Shrub', tree: 'Eucalypt Mallee' },
          img: 'https://live-production.wcms.abc-cdn.net.au/c84d05b9098340f279a981825d31b15a?impolicy=wcms_crop_resize&cropH=3127&cropW=4691&xPos=0&yPos=0&width=862&height=575',
          facts: ['Live in mallee understorey', 'Eat insects and seeds']
        },
        {
          name: 'Orange-bellied Parrot',
          habitat: { soil: 'Grassland Loam', grass: 'Meadow Tussock', shrub: 'Coastal Heath Bush', tree: 'River Red Gum' },
          img: 'https://i0.wp.com/www.australiangeographic.com.au/wp-content/uploads/2021/02/H83TRA-scaled.jpg?fit=2560%2C1707&ssl=1',
          facts: ['Migrate from Tasmania', 'Eat seeds and berries']
        },
        {
          name: 'Mallee Emu-wren',
          habitat: { soil: 'Mallee Loam', grass: 'Spinifex Grass', shrub: 'Mallee Shrub', tree: 'Eucalypt Mallee' },
          img: 'https://i0.wp.com/www.australiangeographic.com.au/wp-content/uploads/2024/10/Mallee-Emu-wren_adjusted-scaled-e1730099610660.jpg?fit=1800%2C1259&ssl=1',
          facts: ['Hide in spinifex grass', 'Very small and colourful']
        }
      ],
      // 动态样式相关
      gardenStyle: {
        background: '#f4a460'
      },
      shrubs: [],
      trees: [],
      animals: [],
      // 动画图标
      showingIcon: false,
      currentIcon: {
        src: '',
        style: {}
      },
      // 对话框状态
      dialogs: {
        feedback: { show: false, text: '' },
        next: { show: false, text: '' },
        congrats: { show: false },
        suggestion: { show: false, text: '' },
        species: { show: false }
      },
      // 当前选中的物种详情
      selectedSpecies: {},
      // 建议相关
      suggestedChange: { type: '', value: '' },
      // confetti相关
      confetti: null
    }
  },
  computed: {
    selectedSpeciesDetail() {
      if (!this.selectedSpecies.habitat) return '';
      return `Habitat: Soil(${this.selectedSpecies.habitat.soil}), 
              Grass(${this.selectedSpecies.habitat.grass}), 
              Shrub(${this.selectedSpecies.habitat.shrub}), 
              Tree(${this.selectedSpecies.habitat.tree})
              <br>${this.selectedSpecies.facts?.join('<br>') || ''}`;
    }
  },
  mounted() {
    // 初始化confetti
    if (window.confetti && this.$refs.confettiCanvas) {
      this.confetti = window.confetti.create(this.$refs.confettiCanvas, { resize: true });
    } else {
      // 加载confetti脚本
      const script = document.createElement('script');
      script.src = "https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js";
      script.onload = () => {
        if (this.$refs.confettiCanvas) {
          this.confetti = window.confetti.create(this.$refs.confettiCanvas, { resize: true });
        }
      };
      document.head.appendChild(script);
    }
  },
  methods: {
    // 显示对话框
    showDialog(type, text, callback) {
      this.dialogs[type].show = true;
      if (text) this.dialogs[type].text = text;
      
      setTimeout(() => {
        this.dialogs[type].show = false;
        if (callback) callback();
      }, 1800);
    },
    
    // 动画图标
    animateIcon(src, flip, callback) {
      this.showingIcon = true;
      this.currentIcon = {
        src,
        style: {
          animation: 'panIcon 3s ease-in-out forwards',
          transform: flip ? 'scaleX(-1)' : 'scaleX(1)'
        }
      };
      
      setTimeout(() => {
        this.showingIcon = false;
        if (callback) callback();
      }, 3000);
    },
    
    // 处理步骤
    handleStep(type, value, iconUrl, flip, nextLabel, plantFn) {
      this.selections[type] = value;
      
      this.animateIcon(iconUrl, flip, () => {
        if (plantFn) plantFn();
        
        this.showDialog('feedback', `Great job! You added ${value}`, () => {
          if (nextLabel) {
            this.showDialog('next', `Now choose your ${nextLabel}!`);
          }
        });
      });
    },
    
    // 具体步骤处理
    handleSoil(value) {
      this.handleStep('soil', value, 'https://png.pngtree.com/png-clipart/20210801/ourmid/pngtree-wheelbarrow-png-image_3768232.jpg', false, 'ground cover', () => {
        this.gardenStyle.background = this.soilColors[value];
      });
    },
    
    handleGrass(value) {
      this.handleStep('grass', value, 'https://png.pngtree.com/png-vector/20240827/ourlarge/pngtree-garden-watering-can-transparent-background-png-image_13629444.png', true, 'shrubs', () => {
        this.gardenStyle.backgroundImage = `url(${this.grassImg})`;
        this.gardenStyle.backgroundSize = '100px 100px';
        this.gardenStyle.backgroundRepeat = 'repeat';
      });
    },
    
    handleShrub(value) {
      this.shrubs = [];
      this.handleStep('shrub', value, 'https://png.pngtree.com/png-vector/20240827/ourlarge/pngtree-garden-watering-can-transparent-background-png-image_13629444.png', true, 'trees', () => {
        // 两个固定的灌木
        const positions = [
          { left: '5%', bottom: '10%' },
          { left: '5%', top: '10%' }
        ];
        
        positions.forEach(pos => {
          this.shrubs.push({
            src: this.shrubImgs[value],
            style: pos
          });
        });
      });
    },
    
    handleTree(value) {
      this.trees = [];
      this.handleStep('tree', value, 'https://png.pngtree.com/png-vector/20240827/ourlarge/pngtree-garden-watering-can-transparent-background-png-image_13629444.png', true, '', () => {
        this.trees.push({
          src: this.treeImgs[value],
          style: { right: '10px', bottom: '-20px' }
        });
      });
    },
    
    // 惊喜按钮
    showSurprise() {
      this.showDialog('congrats', '', () => {
        if (this.confetti) {
          this.confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
          // 播放声音
          const audio = new Audio('https://cdn.pixabay.com/download/audio/2021/08/04/audio_76a1d4b51e.mp3?filename=bells-exciting-6345.mp3');
          audio.play();
        }
        
        setTimeout(this.showAnimals, 2000);
      });
    },
    
    // 显示动物
    showAnimals() {
      this.animals = [];
      this.shrubs = [];
      this.trees = [];
      
      // 找到匹配的物种
      const matches = this.species.filter(s =>
        Object.keys(this.selections).every(k => s.habitat[k] === this.selections[k])
      );
      
      if (matches.length) {
        matches.forEach((s, i) => {
          this.animals.push({
            ...s,
            style: {
              top: `calc(50% - 200px + ${i * 350}px)`,
              left: 'calc(50% - 150px)'
            }
          });
        });
      } else {
        // 找最接近的
        let best = { diff: 5, spec: null };
        this.species.forEach(s => {
          const d = Object.keys(this.selections).reduce((a, k) => a + (s.habitat[k] !== this.selections[k]), 0);
          if (d < best.diff) best = { diff: d, spec: s };
        });
        
        // 找到需要更改的属性
        const comp = Object.keys(this.selections).find(k => best.spec.habitat[k] !== this.selections[k]);
        this.suggestedChange = { type: comp, value: best.spec.habitat[comp] };
        
        this.dialogs.suggestion.text = `Swap ${comp} to "${best.spec.habitat[comp]}"?`;
        this.dialogs.suggestion.show = true;
      }
    },
    
    // 确认建议
    confirmSuggestion() {
      this.dialogs.suggestion.show = false;
      this.selections[this.suggestedChange.type] = this.suggestedChange.value;
      this.showSurprise();
    },
    
    // 取消建议
    cancelSuggestion() {
      this.dialogs.suggestion.show = false;
    },
    
    // 显示物种详情
    showSpeciesDetail(species) {
      this.selectedSpecies = species;
      this.dialogs.species.show = true;
    },
    
    // 关闭物种详情
    closeSpeciesModal() {
      this.dialogs.species.show = false;
    }
  }
}
</script>

<style scoped>
body { margin: 0; padding: 0; font-family: 'Inter', sans-serif; background: #e0f7fa; }
#game-container { display: flex; height: 90vh; margin: 20px; }
#sidebar { width: 240px; background: #ffffff; padding: 1rem; box-shadow: 2px 0 10px rgba(0,0,0,0.1); overflow-y: auto; }
#garden { flex: 1; position: relative; background: #f4a460; overflow: visible; }
.step-title { font-size: 1.25rem; margin-top: 1rem; font-weight: 600; color: #2f4f4f; }
.options { display: flex; flex-direction: column; gap: 0.5rem; margin-top: 0.5rem; }
.options button { padding: 0.6rem; background: #80cbc4; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; transition: background 0.3s; }
.options button:hover { background: #4db6ac; }
#surprise-btn { margin-top: 1.5rem; padding: 0.8rem; background: #ffe082; color: #2f4f4f; border: none; border-radius: 6px; font-size: 1rem; cursor: pointer; font-weight: 700; }
.dialog-overlay { position: fixed; top:0; left:0; width:100%; height:100%; background: rgba(0,0,0,0.5); display:flex; align-items:center; justify-content:center; z-index:200; visibility:hidden; opacity:0; transition: opacity 0.3s; }
.dialog-overlay.show { visibility: visible; opacity: 1; }
.dialog { background: #fff9c4; padding: 1rem 1.5rem; border-radius: 12px; text-align: center; box-shadow: 0 4px 20px rgba(0,0,0,0.2); max-width: 300px; }
.dialog p { margin: 0.5rem 0; font-weight: 600; }
#speciesModal .dialog { max-width: 350px; background: #fff; }
#speciesModal img { width: 100%; height: 150px; object-fit: cover; border-radius: 8px; margin-bottom: 0.5rem; }
#speciesModal h3 { margin: 0.5rem 0; color: #2f4f4f; }
#speciesModal p { font-size: 0.9rem; }
.shrub-item { position: absolute; width: 200px; pointer-events: none; }
.tree-item { position: absolute; width: 500px; pointer-events: none; }
.animal-card { position: absolute; width: 300px; background: rgba(255,255,255,0.9); border-radius: 12px; padding: 1rem; text-align: center; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
.animal-card img { width: 100%; height: 180px; object-fit: cover; border-radius: 8px; }
.animal-card h4 { margin: 0.5rem 0; }
.animal-card small { display: block; margin-top: 0.25rem; font-size: 0.85rem; }
.animal-card button { margin-top: 0.5rem; padding: 0.5rem 1rem; border: none; border-radius: 6px; background: #4db6ac; color: white; cursor: pointer; font-weight: 600; }
.anim-icon { position: absolute; width: 150px; pointer-events: none; }
@keyframes panIcon {
  0% { left: -150px; top: 50%; transform: translateY(-50%) scaleX(1); }
  100% { left: 50%; top: 50%; transform: translate(-50%,-50%) scaleX(1); }
}
#confetti-canvas { position: fixed; top:0; left:0; width:100%; height:100%; pointer-events: none; z-index: 250; }

/* 过渡动画 */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s, transform 0.5s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translateY(20px);
}
</style> 