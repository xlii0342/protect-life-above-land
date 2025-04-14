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
    
    <div style="background-color: #f5f5f5; padding: 1rem; border-radius: 8px; margin-top: 2rem; border-left: 4px solid var(--primary);">
      <h3>Find Regulations for Your Area</h3>
      <p>Cat management regulations may vary between municipalities. Contact your local council to learn about specific regulations for your area.</p>
      <!-- 用按钮替换原来的链接 -->
      <button @click="getCouncilInfo" class="btn" style="margin-top: 1rem;">Find My Local Council</button>
    </div>
    
    <!-- 如果需要显示地图，则在下面显示一个地图容器 -->
    <!-- 地图显示容器：v-show 而不是 v-if -->
    <div v-show="showMap" style="margin-top: 1rem;">
      <div id="map" style="height: 400px; border-radius: 8px;"></div>
    </div>


    
    <!-- 显示获取到的 Council 信息 -->
    <div v-if="councilName" style="margin-top: 1rem;">
      <p>📍 Your Local Council is: <strong>{{ councilName }}</strong></p>
    </div>
    
    <!-- 以下部分保持原有内容 -->
    
    
    <div style="margin-top: 3rem;">
      <h2>Questions?</h2>
      <p>If you have any questions about responsible cat ownership, please feel free to contact our team.</p>
      <div style="margin-top: 1rem;">
        <a href="mailto:info@pawsitive.org" class="btn" style="display: inline-block; text-decoration: none;">Contact Us</a>
      </div>
    </div>
  </div>
</template>

<script>
import 'ol/ol.css'
import { Map, View } from 'ol'
import TileLayer from 'ol/layer/Tile'
import OSM from 'ol/source/OSM'
import { fromLonLat } from 'ol/proj'
import Geocoder from 'ol-geocoder'

export default {
  name: 'Regulations',
  data() {
    return {
      showMap: false,      // 控制地图容器是否显示
      map: null,           // 保存 OpenLayers 地图实例
      councilName: ''      // 存储获取到的 Council 名称
    }
  },
  methods: {
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

          this.showMap = true;
          console.log("✅ showMap is true, should render #map");

          this.$nextTick(() => {
            if (!this.map) {
              console.log("✅ DOM updated, initializing map...");
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
              })

              // 添加 ol-geocoder 搜索控件
              const geocoder = new Geocoder('nominatim', {
                provider: 'osm',
                lang: 'en-US',
                placeholder: 'Search for a location...',
                limit: 5,
                debug: false,
                autoComplete: true,
                autoCompleteMinLength: 2,
                keepOpen: false
              })
              this.map.addControl(geocoder)

              // 地址选择回调
              geocoder.on('addresschosen', evt => {
                this.map.getView().setCenter(evt.coordinate)
                this.map.getView().setZoom(14)
              })
            } else {
              this.map.getView().setCenter(centerCoordinate)
            }
          })

          // 调用 Nominatim API 获取地理信息
          const url = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}&addressdetails=1`
          fetch(url)
            .then(response => response.json())
            .then(data => {
              if (data.address) {
                const council = data.address.municipality || data.address.county || data.address.state_district || 'Not found'
                this.councilName = council
              } else {
                this.councilName = 'Not found'
              }
            })
            .catch(error => {
              console.error('Error fetching Nominatim data:', error)
              alert("Failed to retrieve council information.")
            })
        },
        error => {
          alert("Error getting geolocation: " + error.message)
        }
      )
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
  height: auto;
  display: flex;
  flex-direction: column;
}

.card h3 {
  color: var(--primary);
  margin-bottom: 0.5rem;
  font-size: 1.3rem;
  text-align: left;
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
  color: white !important;
  text-decoration: none;
}

@media (max-width: 768px) {
  .grid-2 {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
}
</style>
