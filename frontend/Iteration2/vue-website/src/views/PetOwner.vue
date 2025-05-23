<template>
  <div class="pet-owner">


    <div class="container">
      <div class="intro-section">
        <div class="intro-quote">
          <span class="quote-mark">"</span>
          <p>Not Just Feral Cats — Indoor Cats Also Need  Management</p>
          <span class="quote-mark closing">"</span>
        </div>
        <div class="intro-highlight">
          <div class="highlight-line"></div>
          <p>Protecting Wildlife Starts at Home — Responsible Cat Ownership Matters</p>
          <div class="highlight-line"></div>
        </div>
      </div>
      
      <div style="margin-top: 2rem;">
        <div class="tab-buttons">
          <button class="tab-button" :class="{ active: activeTab === 'best-practices' }" @click="activeTab = 'best-practices'">Best Practices</button>
          <button class="tab-button" :class="{ active: activeTab === 'containment' }" @click="activeTab = 'containment'">Containment Solutions</button>
          <button class="tab-button" :class="{ active: activeTab === 'regulations' }" @click="activeTab = 'regulations'">Regulations</button>
          <button class="tab-button" :class="{ active: activeTab === 'desexing-microchipping' }" @click="activeTab = 'desexing-microchipping'">Desexing & Microchipping</button>
        </div>
        
        <div class="tab-content" :class="{ active: activeTab === 'best-practices' }">
          <BestPractices v-if="activeTab === 'best-practices'" />
        </div>
            
        <div class="tab-content" :class="{ active: activeTab === 'containment' }">
          <ContainmentSolutions v-if="activeTab === 'containment'" />
        </div>
        
        <div class="tab-content" :class="{ active: activeTab === 'regulations' }">
          <Regulations v-if="activeTab === 'regulations'" />
        </div>
        
        <div class="tab-content" :class="{ active: activeTab === 'desexing-microchipping' }">
          <DesexingMicrochipping v-if="activeTab === 'desexing-microchipping'" />
        </div>
      </div>
      
      <div class="cta">
        Responsible cat ownership satisfies both pet and local wildlife needs - a win-win situation!
      </div>
      
      <div style="margin-top: 3rem;">
        <h2>Questions?</h2>
        <p>If you have any questions about responsible cat ownership, please feel free to contact our team.</p>
        <div style="margin-top: 1rem;">
          <a href="mailto:info@pawsitive.org" class="btn" style="display: inline-block; text-decoration: none;">Contact Us</a>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import BestPractices from '@/components/pet-owner/BestPractices.vue'
import ContainmentSolutions from '@/components/pet-owner/ContainmentSolutions.vue'
import Regulations from '@/components/pet-owner/Regulations.vue'
import DesexingMicrochipping from '@/components/pet-owner/DesexingMicrochipping.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'PetOwner',
  components: {
    BestPractices,
    ContainmentSolutions,
    Regulations,
    DesexingMicrochipping,
    Footer
  },
  data() {
    return {
      activeTab: 'best-practices',
      showDesexingDetails: false,
      showMicrochipDetails: false,
      showDIYModal: false
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

.pet-owner {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 1rem;
  width: 100%;
  box-sizing: border-box;
}

.header {
  background-color: var(--accent);
  padding: 2rem;
  border-radius: 10px;
  margin: 0 auto 2rem;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
  width: 100%;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
}

.header h1 {
  margin: 0;
  font-size: 2.5rem;
  color: white;
  white-space: nowrap;
}

.container {
  background-color: transparent;
  padding: 2rem;
  border-radius: 10px;

  box-shadow: none;
  margin-top: 0;
}

.intro-section {
  text-align: center;
  margin: 0 0 0 3rem;
  padding: 1.5rem;
  position: relative;
}

.intro-quote {
  position: relative;
  margin: 2rem auto;
  max-width: 1500px;
}

.intro-quote p {
  font-size: 1.8rem;
  font-weight: 300;
  color: var(--primary);
  line-height: 1.4;
  letter-spacing: 0.5px;
  margin: 0 2rem;
}

.quote-mark {
  font-family: Georgia, serif;
  font-size: 5rem;
  color: rgba(58, 102, 89, 0.15);
  position: absolute;
  line-height: 1;
}

.quote-mark:first-child {
  top: -2rem;
  left: 0;
}

.quote-mark.closing {
  bottom: -3rem;
  right: 0;
}

.intro-highlight {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 2.5rem auto;
  max-width: 700px;
}

.intro-highlight p {
  font-size: 1.2rem;
  color: #555;
  margin: 0 1.5rem;
  font-weight: 400;
  font-style: italic;
  white-space: nowrap;
}

.highlight-line {
  height: 1px;
  background: linear-gradient(to right, transparent, var(--accent), transparent);
  flex-grow: 1;
}

.pet-owner {
  font-family: var(--font-main);
  background-color: #f7f9f8;
  color: #333;
  line-height: 1.6;
}

h1 {
  font-size: 2.5rem;
  color: var(--primary);
  margin-bottom: 2rem;
  text-align: center;
}

h2 {
  margin-top: 2.5rem;
  margin-bottom: 1.5rem;
  color: var(--accent);
  font-size: 1.8rem;
  text-align: left;
}

h3 {
  color: var(--primary);
  font-size: 1.4rem;
  margin-bottom: 1rem;
  margin-top: 1.5rem;
}

h4 {
  color: var(--accent);
  font-size: 1.2rem;
  margin-bottom: 0.8rem;
  margin-top: 1.2rem;
}

.grid-2 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
  margin: 1.5rem 0;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin: 1.5rem 0;
}

.card {
  background: white;
  border-radius: 10px;
  padding: 1.5rem;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  height: 100%;
  display: flex;
  flex-direction: column;
}

.card h3 {
  color: var(--primary);
  margin-bottom: 1rem;
  font-size: 1.3rem;
  text-align: left;
}

.card p {
  margin-bottom: 1rem;
  line-height: 1.6;
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
  margin: 1rem 0;
}

.btn:hover {
  background-color: #1a3a32;
  color: white !important;
}

.cta {
  background: #fff3cd;
  padding: 1.5rem;
  text-align: center;
  font-weight: bold;
  border-radius: 10px;
  margin: 2.5rem 0;
  font-size: 1.2rem;
  border: 2px solid #ffeeba;
  color: #856404;
}

.tab-buttons {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin: 2rem 0 1rem 0;
  justify-content: center;
}

.tab-button {
  padding: 0.8rem 1.5rem;
  background-color: #e0e0e0;
  border: none;
  border-radius: 5px 5px 0 0;
  font-weight: 600;
  cursor: pointer;
  transition: 0.3s;
}

.tab-button.active {
  background-color: white;
  border-bottom: 3px solid var(--accent);
  color: var(--accent);
}

.tab-content {
  display: none;
  padding: 2rem;
  background: white;
  border-radius: 0 5px 5px 5px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  margin-bottom: 2rem;
  overflow: hidden;
  width: 100%;
  box-sizing: border-box;
}

.tab-content.active {
  display: block;
}

/* 确保tab内容不影响外部布局 */
.tab-content >>> h2,
.tab-content >>> p {
  max-width: 100%;
  box-sizing: border-box;
}

.checklist {
  list-style: none;
  margin: 1rem 0;
  padding-left: 0;
}

.checklist li {
  position: relative;
  padding-left: 2rem;
  margin-bottom: 0.75rem;
  line-height: 1.6;
}

.checklist li::before {
  content: "✓";
  color: var(--accent);
  font-weight: bold;
  position: absolute;
  left: 0;
}

.image-container {
  text-align: center;
  margin: 1.5rem 0;
}

.image-container img {
  max-width: 100%;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  margin-bottom: 0.5rem;
}

.image-container p {
  color: #666;
  font-style: italic;
  margin-top: 0.5rem;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.7);
  z-index: 1000;
  overflow-y: auto;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 2rem;
}

.modal-content {
  background-color: white;
  margin: 5% auto;
  padding: 2rem;
  width: 90%;
  max-width: 800px;
  border-radius: 10px;
  position: relative;
}

.close-button {
  position: absolute;
  top: 1rem;
  right: 1.5rem;
  font-size: 1.5rem;
  cursor: pointer;
  color: var(--primary);
}

@media (max-width: 768px) {
  .grid-2, .grid-3 {
    grid-template-columns: 1fr;
  }
  
  .modal-content {
    width: 95%;
    margin: 2% auto;
    padding: 1.5rem;
  }
  
  h1 {
    font-size: 2rem;
  }
  
  h2 {
    font-size: 1.6rem;
  }
  
  h3 {
    font-size: 1.3rem;
  }
  
  .container {
    padding: 1.5rem;
  }
}
</style> 