<template>
  <div class="overlay" :class="{ active: species }" @click="closeModal">
    <div class="modal" @click.stop>
      <button class="close-btn" @click="closeModal">X</button>
      <img v-if="species" :src="species.img" :alt="species.name">
      <h3 v-if="species">{{ species.name }}</h3>
      <div v-if="species">
        <p>{{ species.description }}</p>
        <h3>Distribution & Habitat</h3>
        <p>{{ species.distribution }}</p>
        <h3>Population Status In Victoria</h3>
        <div class="status-scale">
          <span class="status-item" :class="{ active: species.status === 'Vulnerable' }">Vulnerable</span>
          <span class="status-item" :class="{ active: species.status === 'Endangered' }">Endangered</span>
          <span class="status-item" :class="{ active: species.status === 'Critically Endangered' }">Critically Endangered</span>
          <span class="status-item" :class="{ active: species.status === 'Extinct', 'extinct-status': species.status === 'Extinct' }">Extinct</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SpeciesModal',
  props: {
    species: {
      type: Object,
      default: null
    }
  },
  methods: {
    closeModal() {
      this.$emit('close-modal');
    }
  }
}
</script>

<style scoped>
/* 弹窗样式优化 */
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(5px);
  display: none;
  align-items: flex-start;
  justify-content: center;
  z-index: 1000;
  transition: all 0.3s ease;
  padding-top: 80px;
  overflow-y: auto;
}

.overlay.active {
  display: flex;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.modal {
  background: #ffffff;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25);
  border-radius: 16px;
  padding: 2rem;
  width: 90%;
  max-width: 650px;
  position: relative;
  max-height: 85vh;
  overflow-y: auto;
  animation: modalSlideUp 0.4s ease;
  margin-bottom: 80px;
}

@keyframes modalSlideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal img {
  width: 100%;
  height: 340px;
  object-fit: cover;
  border-radius: 12px;
  margin-bottom: 1.5rem;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
}

.modal h3 {
  margin-bottom: 0.75rem;
  color: #2f4f4f;
  font-size: 1.6rem;
}

.modal p {
  margin-bottom: 1.5rem;
  line-height: 1.6;
  color: #333;
}

.close-btn {
  position: absolute;
  top: 15px;
  right: 20px;
  background: #2f4f4f;
  color: white;
  border: none;
  font-size: 1.2rem;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 200;
  transition: all 0.3s ease;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.15);
}

.close-btn:hover {
  background: #1e3838;
  transform: scale(1.1);
}

.status-scale {
  display: flex;
  justify-content: space-between;
  margin: 1.5rem 0;
  background: #f5f5f5;
  border-radius: 8px;
  padding: 0.75rem;
  flex-wrap: nowrap;
  white-space: nowrap;
  overflow-x: auto;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
}

.status-item {
  padding: 0.6rem 1rem;
  border-radius: 6px;
  font-size: 0.9rem;
  opacity: 0.6;
  text-align: center;
  font-weight: 600;
  margin-right: 0.5rem;
  display: inline-block;
  transition: all 0.3s ease;
}

.status-item:last-child {
  margin-right: 0;
}

.status-item.active {
  background: #d32f2f;
  color: white;
  opacity: 1;
  box-shadow: 0 3px 8px rgba(211, 47, 47, 0.25);
}

.extinct-status.active {
  background: #d32f2f !important;
}

/* 响应式适配 */
@media (max-width: 768px) {
  .modal {
    padding: 1.5rem;
  }
  
  .modal img {
    height: 250px;
  }
  
  .modal h3 {
    font-size: 1.4rem;
  }
  
  .status-scale {
    padding: 0.5rem;
  }
  
  .status-item {
    padding: 0.5rem 0.7rem;
    font-size: 0.8rem;
  }
}
</style> 