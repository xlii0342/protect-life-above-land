<template>
  <div id="game-container">
    <div id="sidebar">
      <div id="step1">
        <div class="step-title">Step 1: Choose Soil</div>
        <div class="options">
          <button @click="selectSoil('Shrubland Clay')">Shrubland Clay</button>
          <button @click="selectSoil('Grassland Loam')">Grassland Loam</button>
          <button @click="selectSoil('Mallee Loam')">Mallee Loam</button>
        </div>
      </div>
      <div id="step2">
        <div class="step-title">Step 2: Ground Cover</div>
        <div class="options">
          <button @click="selectGrass('Heath Hummock')">Heath Hummock</button>
          <button @click="selectGrass('Meadow Tussock')">Meadow Tussock</button>
          <button @click="selectGrass('Spinifex Grass')">Spinifex Grass</button>
        </div>
      </div>
      <div id="step3">
        <div class="step-title">Step 3: Shrubs</div>
        <div class="options">
          <button @click="selectShrub('Mallee Shrub')">Mallee Shrub</button>
          <button @click="selectShrub('Coastal Heath Bush')">Coastal Heath Bush</button>
        </div>
      </div>
      <div id="step4">
        <div class="step-title">Step 4: Trees</div>
        <div class="options">
          <button @click="selectTree('Eucalypt Mallee')">Eucalypt Mallee</button>
          <button @click="selectTree('River Red Gum')">River Red Gum</button>
        </div>
      </div>
      <button id="surprise-btn" @click="showSurprise">Click here for a surprise!</button>
    </div>
    <div id="garden" ref="garden">
      <img v-for="(shrub, i) in shrubs" :key="'shrub-'+i" :src="shrub.src" class="shrub-item" :style="shrub.style" />
      <img v-for="(tree, i) in trees" :key="'tree-'+i" :src="tree.src" class="tree-item" :style="tree.style" />
      <transition-group name="fade">
        <div v-for="(animal, i) in animals" :key="animal.name" class="animal-card" :style="animal.style">
          <img :src="animal.img" />
          <h4>{{ animal.name }}</h4>
          <small>{{ animal.facts[0] }}</small>
          <button @click="showSpeciesDetail(animal)">Learn more!</button>
        </div>
      </transition-group>
      <img v-if="showingIcon" :src="currentIcon.src" class="anim-icon" :style="currentIcon.style" />
    </div>

    <!-- Dialogs -->
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
        <img :src="selectedSpecies.img" alt="" />
        <h3>{{ selectedSpecies.name }}</h3>
        <p v-html="selectedSpeciesDetail"></p>
        <button @click="closeSpeciesModal">Okay!</button>
      </div>
    </div>

    <canvas id="confetti-canvas" ref="confettiCanvas"></canvas>
    <audio ref="confettiSound" :src="confettiSoundSrc"></audio>
  </div>
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
        'Mallee Shrub': 'https://img.freepik.com/free-psd/lush-green-shrubbery-3d-render-vibrant-foliage_191095-91261.jpg',
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
      shrubs: [],
      trees: [],
      animals: [],
      showingIcon: false,
      currentIcon: { src: '', style: {} },
      dialogs: {
        feedback: { show: false, text: '' },
        next: { show: false, text: '' },
        congrats: { show: false },
        suggestion: { show: false, text: '' },
        species: { show: false }
      },
      selectedSpecies: {},
      suggestedChange: { type: '', value: '' },
      confetti: null,
      confettiSoundSrc: 'https://cdn.pixabay.com/download/audio/2021/08/04/audio_76a1d4b51e.mp3?filename=bells-exciting-6345.mp3'
    }
  },
  computed: {
    selectedSpeciesDetail() {
      if (!this.selectedSpecies.habitat) return '';
      return `Habitat: Soil(${this.selectedSpecies.habitat.soil}), Grass(${this.selectedSpecies.habitat.grass}), Shrub(${this.selectedSpecies.habitat.shrub}), Tree(${this.selectedSpecies.habitat.tree})<br>${this.selectedSpecies.facts.join('<br>')}`;
    }
  },
  mounted() {
    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js';
    script.onload = () => {
      if (this.$refs.confettiCanvas) {
        this.confetti = window.confetti.create(this.$refs.confettiCanvas, { resize: true });
      }
    };
    document.head.appendChild(script);
  },
  methods: {
    showDialog(type, text, cb) {
      this.dialogs[type].show = true;
      if (text) this.dialogs[type].text = text;
      setTimeout(() => {
        this.dialogs[type].show = false;
        cb && cb();
      }, 1800);
    },
    animateIcon(src, flip, cb) {
      this.showingIcon = true;
      this.currentIcon = {
        src,
        style: { animation: 'panIcon 3s ease-in-out forwards', transform: flip ? 'scaleX(-1)' : 'scaleX(1)' }
      };
      setTimeout(() => {
        this.showingIcon = false;
        cb && cb();
      }, 3000);
    },
    selectSoil(value) {
      this.selections.soil = value;
      this.animateIcon('https://png.pngtree.com/png-clipart/20210801/ourmid/pngtree-wheelbarrow-png-image_3768232.jpg', false, () => {
        this.$refs.garden.style.background = this.soilColors[value];
        this.showDialog('feedback', `Great job! You added ${value}`, () => this.showDialog('next', 'Now choose your ground cover!'));
      });
    },
    selectGrass(value) {
      this.selections.grass = value;
      this.animateIcon('https://png.pngtree.com/png-vector/20240827/ourlarge/pngtree-garden-watering-can-transparent-background-png-image_13629444.png', true, () => {
        Object.assign(this.$refs.garden.style, {
          backgroundImage: `url(${this.grassImg})`,
          backgroundSize: '100px 100px',
          backgroundRepeat: 'repeat'
        });
        this.showDialog('feedback', `Great job! You added ${value}`, () => this.showDialog('next', 'Now choose your shrubs!'));
      });
    },
    selectShrub(value) {
      this.selections.shrub = value;
      this.shrubs = [];
      this.animateIcon('https://png.pngtree.com/png-vector/20240827/ourlarge/pngtree-garden-watering-can-transparent-background-png-image_13629444.png', true, () => {
        const pos = [
          { left: '5%', bottom: '10%' },
          { left: '5%', top: '10%' }
        ];
        pos.forEach(p => this.shrubs.push({ src: this.shrubImgs[value], style: p }));
        this.showDialog('feedback', `Great job! You added ${value}`, () => this.showDialog('next', 'Now choose your trees!'));
      });
    },
    selectTree(value) {
      this.selections.tree = value;
      this.trees = [];
      this.animateIcon('https://png.pngtree.com/png-vector/20240827/ourlarge/pngtree-garden-watering-can-transparent-background-png-image_13629444.png', true, () => {
        this.trees.push({ src: this.treeImgs[value], style: { right: '10px', bottom: '-20px' } });
        this.showDialog('feedback', `Great job! You added ${value}`, () => {});
      });
    },
    showSurprise() {
      this.showDialog('congrats', '', () => {
        this.confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
        this.$refs.confettiSound.play();
        setTimeout(this.showAnimals, 2000);
      });
    },
    showAnimals() {
      this.animals = [];
      this.shrubs = [];
      this.trees = [];
      const matches = this.species.filter(s => Object.keys(this.selections).every(k => s.habitat[k] === this.selections[k]));
      if (matches.length) {
        matches.forEach((s, i) => this.animals.push({ ...s, style: { top: `calc(50% - 200px + ${i*350}px)`, left: 'calc(50% - 150px)' } }));
      } else {
        let best = { diff: 5, spec: null };
        this.species.forEach(s => {
          const d = Object.keys(this.selections).reduce((a,k) => a + (s.habitat[k] !== this.selections[k]), 0);
          if (d < best.diff) best = { diff: d, spec: s };
        });
        const comp = Object.keys(this.selections).find(k => best.spec.habitat[k] !== this.selections[k]);
        this.dialogs.suggestion.text = `Swap ${comp} to "${best.spec.habitat[comp]}"?`;
        this.dialogs.suggestion.show = true;
      }
    },
    confirmSuggestion() {
      const comp = Object.keys(this.selections).find(k => !!this.dialogs.suggestion.text.includes(k));
      this.selections[comp] = this.species.find(s => s.habitat[k] === this.selections[k]).habitat[comp];
      this.dialogs.suggestion.show = false;
      this.showSurprise();
    },
    cancelSuggestion() { this.dialogs.suggestion.show = false; },
    showSpeciesDetail(s) {
      this.selectedSpecies = s;
      this.dialogs.species.show = true;
    },
    closeSpeciesModal() { this.dialogs.species.show = false; }
  }
}
</script>

<style scoped>
body { margin: 0; padding: 0; font-family: 'Inter', sans-serif; background: #e0f7fa; }
#game-container { display: flex; height: 100vh; }
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
</style>
