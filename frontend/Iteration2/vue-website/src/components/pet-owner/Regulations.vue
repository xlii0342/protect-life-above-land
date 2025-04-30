<template>
  <div class="regulations">
    <h2>Cat Regulations in Victoria</h2>
    
    <div class="grid-2">
      <div class="card">
        <h3>State Regulations</h3>
        <p>According to the Domestic Animals Act:</p>
        <ul class="checklist">
          <li>All cats must be desexed by 6 months of age</li>
          <li>All cats must be microchipped and registered</li>
          <li>In declared areas, cats must be confined to the owner's property 24 hours a day</li>
        </ul>
      </div>
      
      <div class="card">
        <h3>Penalties for Non-Compliance</h3>
        <p>Failing to comply with cat regulations can result in penalties:</p>
        <table style="width: 100%; border-collapse: collapse; margin-top: 1rem;">
          <tr style="background-color: #f0f5f3;">
            <th style="text-align: left; padding: 0.5rem; border: 1px solid #ddd;">Violation</th>
            <th style="text-align: left; padding: 0.5rem; border: 1px solid #ddd;">Fine (AUD)</th>
          </tr>
          <tr>
            <td style="padding: 0.5rem; border: 1px solid #ddd;">Unregistered/unmicrochipped cat</td>
            <td style="padding: 0.5rem; border: 1px solid #ddd;">$330+</td>
          </tr>
          <tr>
            <td style="padding: 0.5rem; border: 1px solid #ddd;">Cat at large in restricted area</td>
            <td style="padding: 0.5rem; border: 1px solid #ddd;">$180+</td>
          </tr>
        </table>
      </div>
    </div>
    
    <!-- 查找区域说明及按钮 -->
    <div style="background-color: #f5f5f5; padding: 1rem; border-radius: 8px; margin-top: 2rem; border-left: 4px solid var(--primary);">
      <h3>Find Regulations for Your Area</h3>
      <p>Cat management regulations may vary between municipalities. Click the button below to display the map and search bar.</p>
      <button @click="getCouncilInfo" class="btn" style="margin-top: 1rem;">Find My Local Council</button>
    </div>
    
    <!-- 显示地图和搜索栏（仅当 showMap 为 true 时显示） -->
    <div v-if="showMap" style="margin-top: 1rem;">
      <!-- 搜索栏（在地图上方） -->
      <div style="margin-bottom: 1rem;">
        <input type="text" v-model="searchQuery" placeholder="Enter location or council..." style="padding: 0.5rem; width: 70%;" />
        <button @click="searchCouncil" class="btn" style="padding: 0.5rem 1rem;">Search</button>
      </div>
      <!-- 地图容器 -->
      <div id="map" style="height: 400px; border-radius: 8px;"></div>
    </div>
    
    <!-- 显示搜索到的 Council 信息 -->
    <div v-if="councilName" style="margin-top: 1rem;">
      <p>📍 Your Local Council is: <strong>{{ councilName }}</strong></p>
    </div>
  </div>
</template>

<script>
import 'ol/ol.css'
import { Map, View } from 'ol'
import TileLayer from 'ol/layer/Tile'
import OSM from 'ol/source/OSM'
import { fromLonLat } from 'ol/proj'

export default {
  name: 'Regulations',
  data() {
    return {
      showMap: false,      // 控制地图容器和搜索栏是否显示
      map: null,           // 存储 OpenLayers 地图实例
      councilName: '',     // 存储获取到的 Council 信息
      searchQuery: ''      // 搜索栏输入的内容
    }
  },
  methods: {
    // 点击 "Find My Local Council" 按钮时调用：显示地图和预定位
    getCouncilInfo() {
      if (!navigator.geolocation) {
        alert("Geolocation is not supported by your browser.");
        return;
      }
      navigator.geolocation.getCurrentPosition(
        position => {
          const latitude = position.coords.latitude;
          const longitude = position.coords.longitude;
          const centerCoordinate = fromLonLat([longitude, latitude]);
          
          // 显示地图和搜索栏
          this.showMap = true;
          console.log("✅ showMap is set to true");

          // 延迟初始化地图，确保 DOM 已渲染
          this.$nextTick(() => {
            if (!this.map) {
              console.log("✅ Initializing map...");
              this.map = new Map({
                target: 'map',
                layers: [
                  new TileLayer({
                    source: new OSM()
                  })
                ],
                view: new View({
                  center: centerCoordinate,
                  zoom: 13
                })
              });
            } else {
              this.map.getView().setCenter(centerCoordinate);
            }
          });

          // 可选：同时可调用反向地理编码获取当前位置信息
          const url = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}&addressdetails=1`;
          fetch(url)
            .then(response => response.json())
            .then(data => {
              if (data.address) {
                const council = data.address.municipality || data.address.county || data.address.state_district || 'Not found';
                this.councilName = council;
              } else {
                this.councilName = 'Not found';
              }
            })
            .catch(error => {
              console.error('Error fetching Nominatim data:', error);
              alert("Failed to retrieve council information.");
            });
        },
        error => {
          alert("Error getting geolocation: " + error.message);
        }
      )
    },
    // 点击搜索按钮时调用：基于输入查询定位并更新地图及显示相关信息
    searchCouncil() {
      if (!this.searchQuery) {
        alert("Please enter a location or council name.");
        return;
      }
      const query = encodeURIComponent(this.searchQuery);
      const url = `https://nominatim.openstreetmap.org/search?format=json&q=${query}&addressdetails=1&limit=1`;

      fetch(url)
        .then(response => response.json())
        .then(data => {
          if (data.length > 0) {
            const result = data[0];
            // 更新 councilName 显示搜索结果
            if (result.address) {
              const council = result.address.municipality || result.address.county || result.address.state_district || 'Not found';
              this.councilName = council;
            } else {
              this.councilName = 'Not found';
            }
            // 根据搜索结果更新地图中心
            const lon = parseFloat(result.lon);
            const lat = parseFloat(result.lat);
            const centerCoordinate = fromLonLat([lon, lat]);
            this.$nextTick(() => {
              if (!this.map) {
                this.map = new Map({
                  target: 'map',
                  layers: [
                    new TileLayer({
                      source: new OSM()
                    })
                  ],
                  view: new View({
                    center: centerCoordinate,
                    zoom: 13
                  })
                });
              } else {
                this.map.getView().setCenter(centerCoordinate);
              }
            });
          } else {
            alert("No results found for the entered location.");
          }
        })
        .catch(error => {
          console.error("Error during search:", error);
          alert("Failed to search for the location.");
        });
    }
  }
}
</script>





<style scoped>
:root {
  --primary: #2f4f4f;
  --accent: #3a6659;
  --highlight: #fcd34d;
  --font-main: 'Inter', sans-serif;
}

.regulations {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  margin: 1.5rem 0;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

.card {
  background: white;
  border-radius: 10px;
  padding: 1rem;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  display: flex;
  flex-direction: column;
}

.card h3 {
  color: var(--primary);
  margin-bottom: 0.5rem;
  font-size: 1.3rem;
}

.card p {
  margin-bottom: 0.5rem;
}

.checklist {
  list-style: none;
  margin: 0.5rem 0;
  padding-left: 0;
}

.checklist li {
  position: relative;
  padding-left: 2rem;
  margin-bottom: 0.5rem;
  line-height: 1.4;
}

.checklist li::before {
  content: "✓";
  color: var(--accent);
  font-weight: bold;
  position: absolute;
  left: 0;
}

.btn {
  background-color: #2c4f46;
  color: white !important;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 5px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  display: inline-block;
  transition: 0.3s;
}

.btn:hover {
  background-color: #1a3a32;
}

@media (max-width: 768px) {
  .grid-2 {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
}
</style>
