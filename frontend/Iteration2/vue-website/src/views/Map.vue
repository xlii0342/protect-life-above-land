<template>
  <div class="map-page">
    <h1 class="page-title">Interactive Maps
    </h1>
    
    <div class="map-selection">
      <button 
        v-for="(section, index) in mapSections" 
        :key="index"
        @click="activeSection = section.id"
        :class="{ active: activeSection === section.id }"
        class="map-selector-btn"
      >
        {{ section.title }}
      </button>
    </div>
    
    <div class="map-container">
      <!-- Feral Cats Section -->
      <div v-if="activeSection === 'feralcats'" class="map-section">
        <h2>Feral Cat Distribution
        <!-- Information Icon -->
        <span class="info-icon" title="Atlas of Living Australia">
          ⓘ
          <div class="info-tooltip">
            Data Source: Atlas of Living Australia. <br>
            Visit <a href="https://www.ala.org.au/" target="_blank">Atlas of Living Australia</a> for more details.
          </div>
        </span>
        </h2>
        <p class="section-description">
          This map shows the distribution and density of feral cats across Victoria, highlighting areas of concern and population hotspots.
          Feral cats have significant impacts on native wildlife and understanding their distribution helps target conservation efforts.
        </p>
        <div class="map-wrapper">
          <div class="map" ref="feralCatsMap"></div>
          <div class="map-legend">
            <h3>Legend</h3>
            <div class="legend-item">
              <span class="color-indicator high"></span>
              <span>High Density (>10 cats/km²)</span>
            </div>
            <div class="legend-item">
              <span class="color-indicator medium"></span>
              <span>Medium Density (5-10 cats/km²)</span>
            </div>
            <div class="legend-item">
              <span class="color-indicator low"></span>
              <span>Low Density (<5 cats/km²)</span>
            </div>
          </div>
        </div>
        <div class="map-info">
          <h3>Impact of Feral Cats</h3>
          <p>
            Feral cats are one of the most significant threats to Victoria's native wildlife. They are effective predators 
            that hunt and kill a wide range of animals including birds, mammals, reptiles, and insects. A single feral cat 
            can kill up to 1,000 native animals each year, contributing significantly to population declines and extinctions.
          </p>
          <p>
            Areas with higher feral cat density (shown in red) correlate with declining populations of threatened species, 
            particularly small to medium-sized mammals and ground-nesting birds.
          </p>
        </div>
      </div>
      
      <!-- Endangered Animals Section -->
      <div v-if="activeSection === 'endangered'" class="map-section">
        <h2>Endangered Species Distribution
        <!-- Information Icon -->
        <span class="info-icon" title="Atlas of Living Australia">
          ⓘ
          <div class="info-tooltip">
            Data Source: Atlas of Living Australia. <br>
            Visit <a href="https://www.ala.org.au/" target="_blank">Atlas of Living Australia</a> for more details.
          </div>
        </span>
        </h2>
        <p class="section-description">
          This map shows the distribution of endangered and threatened species across Victoria, 
          highlighting biodiversity hotspots and critical habitats that require protection.
        </p>
        <div class="map-wrapper">
          <div class="map" ref="endangeredMap"></div>
          <div class="map-legend">
            <h3>Legend</h3>
            <div class="legend-item">
              <span class="color-indicator critical"></span>
              <span>Critically Endangered Species</span>
            </div>
            <div class="legend-item">
              <span class="color-indicator endangered"></span>
              <span>Endangered Species</span>
            </div>
            <div class="legend-item">
              <span class="color-indicator vulnerable"></span>
              <span>Vulnerable Species</span>
            </div>
          </div>
        </div>
        <div class="map-info">
          <h3>Biodiversity Hotspots</h3>
          <p>
            Victoria is home to numerous endemic species found nowhere else in the world. These biodiversity hotspots
            are critical for conservation efforts. The map highlights areas where multiple threatened species coexist,
            making these regions priorities for habitat protection and feral cat management.
          </p>
          <p>
            Click on specific regions to see detailed information about the endangered species present in that area.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue';
import * as L from 'leaflet';
import Papa from 'papaparse'; // Import PapaParse for CSV parsing

export default {
  name: 'MapView',
  setup() {
    const activeSection = ref('feralcats');
    const feralCatsMap = ref(null);
    const endangeredMap = ref(null);
    
    const mapSections = [
      { id: 'feralcats', title: 'Feral Cats Distribution' },
      { id: 'endangered', title: 'Endangered Animals' }
    ];

    const initMap = (mapRef, center = [-37.8136, 144.9631], zoom = 7) => {
      if (!mapRef.value) return null;

      console.log(`Initializing map for ref: ${mapRef.value}`);

      // Initialize the map
      const map = L.map(mapRef.value).setView(center, zoom);
      
      // Add OpenStreetMap tile layer
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map);
      
      return map;
    };

    const fetchFeralCatData = async () => {
      try {
        const response = await fetch('/assets/data/feral_cats_with_density.csv');
        const csvText = await response.text();

        const parsedData = Papa.parse(csvText, {
          header: true,
          skipEmptyLines: true,
        });

        return parsedData.data;
      } catch (error) {
        console.error('Failed to fetch or parse feral cat data:', error);
        return [];
      }
    };

    const fetchEndangeredSpeciesData = async () => {
      try {
        const response = await fetch('/assets/data/complete_endangered_species.csv');
        const csvText = await response.text();
        const parsedData = Papa.parse(csvText, {
          header: true,
          skipEmptyLines: true,
        });
        console.log('Fetched endangered species data:', parsedData.data);
        return parsedData.data;
      } catch (error) {
        console.error('Failed to fetch or parse species data:', error);
        return [];
      }
    };

    const addFeralCatMarkers = (map, data) => {
      data.forEach((cat) => {
        const density = cat.Density || 'unknown'; // Adjust as per your CSV column names
        const markerColor =
          density === 'high'
            ? '#d62828'
            : density === 'medium'
            ? '#f77f00'
            : density === 'low'
            ? '#fcbf49'
            : '#cccccc';

        const marker = L.circleMarker([cat.Latitude, cat.Longitude], {
          radius: 5,
          fillColor: markerColor,
          color: '#fff',
          weight: 1,
          opacity: 1,
          fillOpacity: 0.8,
        }).addTo(map);

        marker.bindPopup(`
          Location: ${cat.Local_Government_Area || 'Unknown Location'}<br>
          Feral Cat Density: ${cat.Density.charAt(0).toUpperCase() + cat.Density.slice(1)}<br>
          Individual Count: ${cat.Individual_Count}<br>
          Date: ${cat.Date}
        `);
      });
    };

    const addEndangeredMarkers = (map, data) => {
      if (!data || data.length === 0) {
        console.warn('No endangered species data available to render markers');
        return;
      }

      console.log('Adding endangered species markers:', data);

      data.forEach((species) => {
        const markerColor =
          species["Category of Threat"] === "Critically Endangered"
            ? "#d62828"
            : species["Category of Threat"] === "Endangered"
            ? "#f77f00"
            : species["Category of Threat"] === "Vulnerable"
            ? "#fcbf49"
            : "#cccccc";

        const marker = L.circleMarker([parseFloat(species.Latitude), parseFloat(species.Longitude)], {
          radius: 5,
          fillColor: markerColor,
          color: "#fff",
          weight: 1,
          opacity: 1,
          fillOpacity: 0.8,
        }).addTo(map);

        marker.bindPopup(`
          <strong>${species.Common_Name || "Unknown Species"}</strong><br>
          Scientific Name: ${species.Scientific_Name || "Unknown"}<br>
          Status: ${species["Category of Threat"] || "Unknown"}<br>
          Extinction Risk: ${species["Extinction Risk"] || "Unknown"}<br>
          Recorded Date: ${species.Date || "Unknown"}
        `);
      });
    };

    onMounted(async () => {
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = 'https://unpkg.com/leaflet@1.7.1/dist/leaflet.css';
      document.head.appendChild(link);

      setTimeout(async () => {
        if (feralCatsMap.value) {
          const feralCatsMapInstance = initMap(feralCatsMap);
          if (feralCatsMapInstance) {
            const feralCatData = await fetchFeralCatData();
            addFeralCatMarkers(feralCatsMapInstance, feralCatData);
          }
        }

        if (endangeredMap.value) {
          const endangeredMapInstance = initMap(endangeredMap);
          if (endangeredMapInstance) {
            const speciesData = await fetchEndangeredSpeciesData();
            addEndangeredMarkers(endangeredMapInstance, speciesData);
          }
        }
      }, 500);
    });

    watch(activeSection, (newSection) => {
      setTimeout(() => {
        if (newSection === 'feralcats' && feralCatsMap.value) {
          const map = initMap(feralCatsMap);
          if (map) {
            fetchFeralCatData().then((feralCatData) => {
              addFeralCatMarkers(map, feralCatData);
            });
          }
        } else if (newSection === "endangered" && endangeredMap.value) {
          const map = initMap(endangeredMap);
          if (map) {
            fetchEndangeredSpeciesData().then((speciesData) => {
              addEndangeredMarkers(map, speciesData);
            });
          }
        }
      }, 100);
    });

    return {
      activeSection,
      mapSections,
      feralCatsMap,
      endangeredMap
    };
  }
};
</script>

<style scoped>
.map-page {
  padding: 2rem 1rem;
  max-width: 1200px;
  margin: 0 auto;
}

.page-title {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 2rem;
  font-size: 2.2rem;
}
.info-icon {
  display: inline-block;
  font-size: 1.2rem;
  margin-left: 10px;
  cursor: pointer;
  position: relative;
}

.info-icon:hover .info-tooltip {
  display: block;
}

.info-tooltip {
  display: none;
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  padding: 10px;
  font-size: 0.9rem;
  font-weight: 200; /* Add this to make the font slim */
  line-height: 1.4;
  width: 220px;
  z-index: 10;
  text-align: center;
}

.info-tooltip a {
  color: #3498db;
  text-decoration: none;
}

.info-tooltip a:hover {
  text-decoration: underline;
}

.map-selection {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 2rem;
}

.map-selector-btn {
  padding: 0.8rem 1.5rem;
  background-color: #f0f0f0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.map-selector-btn:hover {
  background-color: #e0e0e0;
}

.map-selector-btn.active {
  background-color: #2a9d8f;
  color: white;
}

.map-section {
  margin-top: 1rem;
}

.map-section h2 {
  color: #2c3e50;
  margin-bottom: 1rem;
  text-align: center;
}

.section-description {
  text-align: center;
  max-width: 800px;
  margin: 0 auto 1.5rem;
  color: #666;
  line-height: 1.6;
}

.map-wrapper {
  display: flex;
  flex-direction: column;
  margin-bottom: 2rem;
}

.map {
  height: 500px;
  width: 100%;
  margin-top: 1rem;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.map-legend {
  background-color: white;
  padding: 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-top: 1rem;
}

.map-legend h3 {
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
  color: #2c3e50;
}

.legend-item {
  display: flex;
  align-items: center;
  margin-bottom: 0.5rem;
}

.color-indicator {
  display: inline-block;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  margin-right: 10px;
}

/* Feral cat density colors */
.color-indicator.high {
  background-color: #d62828;
}

.color-indicator.medium {
  background-color: #f77f00;
}

.color-indicator.low {
  background-color: #fcbf49;
}

/* Endangered species status colors */
.color-indicator.critical {
  background-color: #d62828;
}

.color-indicator.endangered {
  background-color: #f77f00;
}

.color-indicator.vulnerable {
  background-color: #fcbf49;
}

.map-info {
  background-color: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-top: 1rem;
}

.map-info h3 {
  color: #2c3e50;
  margin-top: 0;
  margin-bottom: 1rem;
}

.map-info p {
  margin-bottom: 1rem;
  line-height: 1.6;
  color: #555;
}

@media (min-width: 768px) {
  .map-wrapper {
    flex-direction: row;
  }

  .map {
    flex: 1;
  }

  .map-legend {
    width: 250px;
    margin-top: 0;
    margin-left: 1rem;
  }
}

@media (max-width: 768px) {
  .map-selection {
    flex-direction: column;
    align-items: center;
  }
  
  .map-selector-btn {
    width: 100%;
    max-width: 300px;
  }

  .map {
    height: 400px;
  }
}
</style>