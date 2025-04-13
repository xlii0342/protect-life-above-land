<template>
  <div class="extinct-species-section">
    <div class="extinct-header">
      <h3>They're already <span>EXTINCT</span> because of feral cats ...</h3>
    </div>
    
    <div class="extinct-cards-row">
      <div v-for="(species, index) in extinctSpecies" :key="species.name" 
           class="card extinct-card" 
           @click="showSpeciesDetails(species)">
        <img :src="species.img" :alt="species.name">
        <p>{{ species.name }}</p>
        <span class="extinct-label">Extinct</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ExtinctSpecies',
  props: {
    extinctSpecies: {
      type: Array,
      required: true
    }
  },
  methods: {
    showSpeciesDetails(species) {
      this.$emit('show-species-details', species);
    }
  }
}
</script>

<style scoped>
/* 已灭绝物种部分样式 */
.extinct-species-section {
  margin-bottom: 4rem;
  padding-bottom: 3rem;
  border-bottom: 1px dashed rgba(0, 0, 0, 0.1);
}

.extinct-species-section:last-of-type {
  border-bottom: none;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
}

.extinct-header {
  text-align: center;
  margin-bottom: 2.5rem;
}

.extinct-header h3 {
  font-size: 2.6rem;
  line-height: 1.3;
  color: #333;
  font-weight: 800;
}

.extinct-header h3 span {
  color: #d32f2f;
  font-weight: 900;
  text-shadow: 1px 1px 0 rgba(0,0,0,0.1);
  position: relative;
  display: inline-block;
}

.extinct-header h3 span::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 3px;
  background-color: #d32f2f;
}

/* 灭绝物种横向排列 */
.extinct-cards-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2rem;
  padding: 1rem;
}

/* 卡片样式 */
.card {
  background: #ffffff;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.08);
  cursor: pointer;
  border-radius: 12px;
  overflow: hidden;
  position: relative;
  border: 1px solid rgba(0, 0, 0, 0.05);
  width: 250px;
  transition: all 0.3s ease;
}

.card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 30px rgba(211, 47, 47, 0.25);
}

.card p {
  padding: 1rem 0.75rem 0.5rem;
  margin: 0;
  text-align: center;
  font-weight: 600;
  font-size: 1.1rem;
  color: #2f4f4f;
}

.extinct-card {
  border: 2px solid #d32f2f;
  box-shadow: 0 6px 15px rgba(211, 47, 47, 0.1);
}

.extinct-label {
  display: block;
  font-weight: bold;
  font-size: 0.85rem;
  text-align: center;
  margin: 0 0 0.75rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 0.3rem 0;
  color: #d32f2f;
  background-color: rgba(211, 47, 47, 0.1);
}

.card img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  transition: all 0.3s ease;
}

/* 响应式适配 */
@media (max-width: 768px) {
  .extinct-header h3 {
    font-size: 2rem;
  }
  
  .extinct-cards-row {
    gap: 1.5rem;
  }
  
  .card {
    width: calc(50% - 1rem);
    min-width: 140px;
  }
}

@media (max-width: 480px) {
  .card {
    width: 100%;
  }
}
</style> 