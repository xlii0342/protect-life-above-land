<template>
    <div class="map-page">
      <h1 class="page-title">Interactive Maps</h1>
      
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
          <h2>Feral Cat Distribution</h2>
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
          <h2>Endangered Species Distribution</h2>
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
        
        <!-- Habitat Section -->
        <div v-if="activeSection === 'habitat'" class="map-section">
          <h2>Critical Habitats and Protected Areas</h2>
          <p class="section-description">
            This map displays Victoria's critical habitats, protected areas, and ecological regions 
            important for wildlife conservation, along with habitat loss data and restoration opportunities.
          </p>
          <div class="map-wrapper">
            <div class="map" ref="habitatMap"></div>
            <div class="map-legend">
              <h3>Legend</h3>
              <div class="legend-item">
                <span class="color-indicator protected"></span>
                <span>Protected Conservation Areas</span>
              </div>
              <div class="legend-item">
                <span class="color-indicator critical-habitat"></span>
                <span>Critical Habitat Zones</span>
              </div>
              <div class="legend-item">
                <span class="color-indicator restoration"></span>
                <span>Habitat Restoration Projects</span>
              </div>
            </div>
          </div>
          <div class="map-info">
            <h3>Habitat Conservation</h3>
            <p>
              Habitat loss and fragmentation are major threats to Victoria's biodiversity. Protected areas 
              (shown in green) provide safe havens for native wildlife, while habitat restoration projects 
              (shown in blue) are working to reconnect fragmented landscapes.
            </p>
            <p>
              Critical habitat zones (shown in orange) are areas identified as essential for the survival 
              of endangered species but may not yet have formal protection status.
            </p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted, watch } from 'vue';
  import * as L from 'leaflet';
  
  export default {
    name: 'MapView',
    setup() {
      const activeSection = ref('feralcats');
      const feralCatsMap = ref(null);
      const endangeredMap = ref(null);
      const habitatMap = ref(null);
      
      const mapSections = [
        { id: 'feralcats', title: 'Feral Cats Distribution' },
        { id: 'endangered', title: 'Endangered Animals' },
        { id: 'habitat', title: 'Critical Habitats' }
      ];
  
      const initMap = (mapRef, center = [-37.8136, 144.9631], zoom = 7) => {
        if (!mapRef.value) return null;
  
        // Initialize the map
        const map = L.map(mapRef.value).setView(center, zoom);
        
        // Add OpenStreetMap tile layer
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);
        
        return map;
      };
  
      // Sample data for feral cat distribution (would be replaced with real data)
      const feralCatData = [
        { lat: -37.6813, lng: 144.2844, density: 'high', location: 'Western Victoria' },
        { lat: -37.0502, lng: 143.7175, density: 'high', location: 'Ballarat Region' },
        { lat: -36.7228, lng: 142.1993, density: 'medium', location: 'Grampians' },
        { lat: -37.9712, lng: 145.2119, density: 'low', location: 'Eastern Suburbs' },
        { lat: -38.2383, lng: 144.5192, density: 'medium', location: 'Bellarine Peninsula' },
        { lat: -36.3230, lng: 146.5880, density: 'high', location: 'Northeast Victoria' }
      ];
  
      // Sample data for endangered species (would be replaced with real data)
      const endangeredData = [
        { lat: -37.6813, lng: 144.2844, status: 'critical', species: 'Orange-bellied Parrot' },
        { lat: -38.4105, lng: 142.2731, status: 'endangered', species: 'Eastern Barred Bandicoot' },
        { lat: -36.7228, lng: 142.1993, status: 'vulnerable', species: 'Malleefowl' },
        { lat: -37.9712, lng: 145.2119, status: 'critical', species: 'Southern Bent-wing Bat' },
        { lat: -37.2383, lng: 146.5192, status: 'endangered', species: 'Spot-tailed Quoll' },
        { lat: -36.3230, lng: 146.5880, status: 'vulnerable', species: 'Growling Grass Frog' }
      ];
  
      // Sample data for habitats (would be replaced with real data)
      const habitatData = [
        { lat: -37.6813, lng: 144.2844, type: 'protected', name: 'Organ Pipes National Park' },
        { lat: -38.4105, lng: 142.2731, type: 'critical-habitat', name: 'Coastal Saltmarsh' },
        { lat: -36.7228, lng: 142.1993, type: 'protected', name: 'Grampians National Park' },
        { lat: -37.9712, lng: 145.2119, type: 'restoration', name: 'Dandenong Creek Restoration' },
        { lat: -37.2383, lng: 146.5192, type: 'critical-habitat', name: 'Alpine Bogs' },
        { lat: -36.3230, lng: 146.5880, type: 'restoration', name: 'Murray River Wetlands' }
      ];
  
      const addFeralCatMarkers = (map) => {
        feralCatData.forEach(cat => {
          const markerColor = cat.density === 'high' ? '#d62828' : 
                              cat.density === 'medium' ? '#f77f00' : '#fcbf49';
          
          const marker = L.circleMarker([cat.lat, cat.lng], {
            radius: 10,
            fillColor: markerColor,
            color: '#fff',
            weight: 1,
            opacity: 1,
            fillOpacity: 0.8
          }).addTo(map);
          
          marker.bindPopup(`
            <strong>${cat.location}</strong><br>
            Feral Cat Density: ${cat.density.charAt(0).toUpperCase() + cat.density.slice(1)}
          `);
        });
      };
  
      const addEndangeredMarkers = (map) => {
        endangeredData.forEach(item => {
          const markerColor = item.status === 'critical' ? '#d62828' : 
                             item.status === 'endangered' ? '#f77f00' : '#fcbf49';
          
          const marker = L.circleMarker([item.lat, item.lng], {
            radius: 10,
            fillColor: markerColor,
            color: '#fff',
            weight: 1,
            opacity: 1,
            fillOpacity: 0.8
          }).addTo(map);
          
          marker.bindPopup(`
            <strong>${item.species}</strong><br>
            Status: ${item.status.charAt(0).toUpperCase() + item.status.slice(1)}
          `);
        });
      };
  
      const addHabitatMarkers = (map) => {
        habitatData.forEach(item => {
          const markerColor = item.type === 'protected' ? '#2a9d8f' : 
                             item.type === 'critical-habitat' ? '#e76f51' : '#457b9d';
          
          const marker = L.circleMarker([item.lat, item.lng], {
            radius: 10,
            fillColor: markerColor,
            color: '#fff',
            weight: 1,
            opacity: 1,
            fillOpacity: 0.8
          }).addTo(map);
          
          marker.bindPopup(`
            <strong>${item.name}</strong><br>
            Type: ${item.type.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')}
          `);
        });
      };
  
      // Initialize maps when component is mounted
      onMounted(() => {
        // Need to dynamically import Leaflet CSS
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = 'https://unpkg.com/leaflet@1.7.1/dist/leaflet.css';
        document.head.appendChild(link);
        
        setTimeout(() => {
          const feralCatsMapInstance = initMap(feralCatsMap);
          if (feralCatsMapInstance) {
            addFeralCatMarkers(feralCatsMapInstance);
          }
        }, 500);
      });
  
      // Watch for active section changes to initialize the appropriate map
      watch(activeSection, (newSection) => {
        setTimeout(() => {
          if (newSection === 'feralcats' && feralCatsMap.value) {
            const map = initMap(feralCatsMap);
            if (map) addFeralCatMarkers(map);
          } else if (newSection === 'endangered' && endangeredMap.value) {
            const map = initMap(endangeredMap);
            if (map) addEndangeredMarkers(map);
          } else if (newSection === 'habitat' && habitatMap.value) {
            const map = initMap(habitatMap);
            if (map) addHabitatMarkers(map);
          }
        }, 100);
      });
  
      return {
        activeSection,
        mapSections,
        feralCatsMap,
        endangeredMap,
        habitatMap
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
  
  /* Habitat types colors */
  .color-indicator.protected {
    background-color: #2a9d8f;
  }
  
  .color-indicator.critical-habitat {
    background-color: #e76f51;
  }
  
  .color-indicator.restoration {
    background-color: #457b9d;
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