<template>
  <div class="endangered-category">
    <h2 class="category-header">But we still have chances to save these species</h2>
    
    <!-- 濒危物种卡片 - 每行5张，最多显示10张 -->
    <div class="species-cards-container">
      <div v-for="species in displaySpecies" :key="'species-'+species.id" 
           :class="['card', getCardClass(species)]" 
           @click="showSpeciesDetails(species)">
        <img :src="species.img" :alt="species.name">
        <p>{{ species.name }}</p>
        <span :class="['status-label', getLabelClass(species)]">{{ getStatusLabel(species) }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EndangeredCategory',
  props: {
    criticallyEndangeredSpecies: {
      type: Array,
      required: true
    },
    endangeredSpecies: {
      type: Array,
      required: true
    },
    vulnerableSpecies: {
      type: Array,
      required: true
    }
  },
  computed: {
    // 所有濒危物种列表（按顺序：极危、濒危、易危）
    displaySpecies() {
      // 合并所有类型的物种，并最多显示10个
      const allSpecies = [
        ...this.criticallyEndangeredSpecies.map(species => ({...species, type: 'critical'})),
        ...this.endangeredSpecies.map(species => ({...species, type: 'endangered'})),
        ...this.vulnerableSpecies.map(species => ({...species, type: 'vulnerable'}))
      ];
      
      return allSpecies.slice(0, 10);
    }
  },
  methods: {
    showSpeciesDetails(species) {
      this.$emit('show-species-details', species);
    },
    // 根据物种类型返回卡片CSS类
    getCardClass(species) {
      return `${species.type}-card`;
    },
    // 根据物种类型返回标签CSS类
    getLabelClass(species) {
      return `${species.type}-label`;
    },
    // 根据物种类型返回状态文本
    getStatusLabel(species) {
      switch(species.type) {
        case 'critical': return 'Critically Endangered';
        case 'endangered': return 'Endangered';
        case 'vulnerable': return 'Vulnerable';
        default: return '';
      }
    }
  }
}
</script>

<style scoped>
/* 濒危物种类别样式 */
.endangered-category {
  margin-bottom: 4rem;
  padding-bottom: 3rem;
  border-bottom: 1px dashed rgba(0, 0, 0, 0.1);
}

.endangered-category:last-of-type {
  border-bottom: none;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
}

/* 主标题样式 */
.category-header {
  color: #3a6659;
  font-size: 2.2rem;
  margin: 2rem auto;
  text-align: center;
  font-weight: 700;
  position: relative;
  display: inline-block;
  left: 50%;
  transform: translateX(-50%);
}

.category-header::after {
  content: '';
  position: absolute;
  bottom: -12px;
  left: 0;
  width: 100%;
  height: 4px;
  border-radius: 3px;
  background-color: #3a6659;
}

/* 卡片容器样式 */
.species-cards-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5rem;
  padding: 2rem 1rem;
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
  width: 180px;
  transition: all 0.3s ease;
  flex: 0 0 auto;
  margin-bottom: 1.5rem;
}

.card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
}

.card p {
  padding: 1rem 0.75rem 0.5rem;
  margin: 0;
  text-align: center;
  font-weight: 600;
  font-size: 1.1rem;
  color: #2f4f4f;
}

/* 默认状态不再使用不同颜色的边框 */
.critical-card, .endangered-card, .vulnerable-card {
  border: 2px solid #e0e0e0;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.08);
}

/* 鼠标悬停时显示对应颜色 */
.critical-card:hover {
  border: 2px solid #D32F2F;
  box-shadow: 0 15px 30px rgba(211, 47, 47, 0.25);
}

.endangered-card:hover {
  border: 2px solid #F57C00;
  box-shadow: 0 15px 30px rgba(245, 124, 0, 0.25);
}

.vulnerable-card:hover {
  border: 2px solid #689F38;
  box-shadow: 0 15px 30px rgba(104, 159, 56, 0.25);
}

.status-label {
  display: block;
  font-weight: bold;
  font-size: 0.8rem;
  text-align: center;
  margin: 0 0 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding: 0.3rem 0;
}

.critical-label {
  color: #D32F2F;
  background-color: rgba(211, 47, 47, 0.1);
}

.endangered-label {
  color: #F57C00;
  background-color: rgba(245, 124, 0, 0.1);
}

.vulnerable-label {
  color: #689F38;
  background-color: rgba(104, 159, 56, 0.1);
}

.card img {
  width: 100%;
  height: 160px;
  object-fit: cover;
  transition: all 0.3s ease;
}

/* 响应式适配 */
@media (max-width: 992px) {
  .card {
    width: calc(33.333% - 1rem);
    min-width: 160px;
  }
}

@media (max-width: 768px) {
  .category-header {
    font-size: 1.8rem;
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