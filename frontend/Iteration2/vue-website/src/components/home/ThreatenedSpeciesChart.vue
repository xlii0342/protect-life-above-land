
<template>
    <div class="chart-container">
      <canvas ref="barCanvas"></canvas>
      
      <!-- Modal for displaying additional species information -->
      <div id="overlay" class="overlay" :class="{ active: isModalActive }">
        <div class="modal">
          <div class="modal-header">
            <h3 id="modalTitle">{{ selectedSpecies.commonName }}</h3>
            <button @click="closeModal" class="close-button">×</button>
          </div>
          <div class="modal-body">
            <p id="modalText" v-html="modalContent"></p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted, computed } from 'vue';
  // 更明确的Chart.js导入
  import Chart from 'chart.js/auto';
  
  export default {
    name: 'ThreatenedSpeciesChart',
    props: {
      speciesData: {
        type: Array,
        required: true
      }
    },
    setup(props) {
      const barCanvas = ref(null);
      const chart = ref(null);
      const isModalActive = ref(false);
      const selectedSpecies = ref({
        commonName: '',
        scientificName: '',
        status: '',
        subgroup: ''
      });
  
      const modalContent = computed(() => {
        return `<strong>Scientific Name:</strong> ${selectedSpecies.value.scientificName}<br>
                <strong>Status:</strong> ${selectedSpecies.value.status}<br>
                <strong>Subgroup:</strong> ${selectedSpecies.value.subgroup}`;
      });
  
      const showModal = (commonName, scientificName, status, subgroup) => {
        selectedSpecies.value = {
          commonName,
          scientificName,
          status,
          subgroup
        };
        isModalActive.value = true;
      };
  
      const closeModal = () => {
        isModalActive.value = false;
      };
  
      onMounted(() => {
        // 使用setTimeout确保DOM已完全渲染
        setTimeout(() => {
          if (!barCanvas.value) {
            console.error('Canvas element not found');
            return;
          }
          
          try {
            const ctx = barCanvas.value.getContext('2d');
            if (!ctx) {
              console.error('Could not get canvas context');
              return;
            }
            
            // 清除可能存在的旧图表
            if (chart.value) {
              chart.value.destroy();
            }
            
            // Extract unique subgroups and statuses from the data
            const subgroups = [...new Set(props.speciesData.map(d => d.species_subgroup))];
            const statuses = [...new Set(props.speciesData.map(d => d.status))];
            
            // Prepare datasets for each status
            const datasets = statuses.map(status => ({
              label: status,
              data: subgroups.map(subgroup => {
                const matchingSpecies = props.speciesData.filter(
                  d => d.species_subgroup === subgroup && d.status === status
                );
                return matchingSpecies.length > 0 ? matchingSpecies[0].count : 0;
              }),
              backgroundColor: status === 'Critically Endangered' ? '#d62828' :
                              status === 'Endangered' ? '#f77f00' :
                              status === 'Vulnerable' ? '#fcbf49' : '#6c757d'
            }));
  
            console.log('Creating chart with data:', { labels: subgroups, datasets });
            
            // Create the chart
            chart.value = new Chart(ctx, {
              type: 'bar',
              data: {
                labels: subgroups,
                datasets: datasets
              },
              options: {
                responsive: true,
                maintainAspectRatio: false,  // 允许Chart.js控制尺寸
                plugins: {
                  title: { 
                    display: true, 
                    text: 'Subgroup vs. Category of Threat',
                    font: {
                      size: 16,
                      weight: 'bold'
                    }
                  },
                  legend: { position: 'bottom' }
                },
                scales: {
                  y: { 
                    beginAtZero: true, 
                    ticks: { precision: 0 } 
                  }
                }
              }
            });
          } catch (error) {
            console.error('Error initializing chart:', error);
          }
        }, 300);  // 给DOM足够的时间渲染
      });
  
      return {
        barCanvas,
        isModalActive,
        selectedSpecies,
        modalContent,
        showModal,
        closeModal
      };
    }
  }
  </script>
  
  <style scoped>
  .chart-container {
    width: 100%;
    margin: 20px 0 30px 0;
    position: relative;
    height: 400px;
    overflow: visible;
  }
  
  canvas {
    width: 100% !important;
    height: 100% !important;
    max-height: 400px;
  }
  
  .overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7);
    z-index: 1000;
    justify-content: center;
    align-items: center;
  }
  
  .overlay.active {
    display: flex;
  }
  
  .modal {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    max-width: 600px;
    width: 80%;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
  }
  
  .modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #eee;
    padding-bottom: 10px;
    margin-bottom: 15px;
  }
  
  .modal-header h3 {
    margin: 0;
    font-size: 1.5rem;
    color: #333;
  }
  
  .close-button {
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
    color: #666;
  }
  
  .close-button:hover {
    color: #000;
  }
  
  .visualization-section h2 {
    text-align: center;
    margin-bottom: 25px;
    color: #2c3e50;
  }
  </style> 
  