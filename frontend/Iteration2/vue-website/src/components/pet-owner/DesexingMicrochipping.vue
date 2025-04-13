<template>
  <div class="desexing-microchipping">
    <h2>Desexing and Microchipping</h2>
    
    <div class="section">
      <h3>Desexing Your Cat in Victoria</h3>
      
      <div class="grid-2">
        <div class="info-card">
          <h4>Why Desexing Is Important</h4>
          <p>Desexing your cat is a smart and caring choice that helps both your pet and the community:</p>
          <ul class="checklist" v-if="!expandedLists.desexingWhy">
            <li>Stops surprise litters and helps reduce stray cat numbers across Victoria</li>
            <li>Cuts down the chances of your cat roaming or getting into fights</li>
            <li v-if="!isMobile">Lowers the risk of certain serious health issues, like some cancers</li>
          </ul>
          <ul class="checklist" v-else>
            <li>Stops surprise litters and helps reduce stray cat numbers across Victoria</li>
            <li>Cuts down the chances of your cat roaming or getting into fights</li>
            <li>Lowers the risk of certain serious health issues, like some cancers</li>
            <li>Can lead to a more chilled and affectionate cat at home</li>
            <li>It's the law in Victoria for cats older than 6 months to be desexed</li>
          </ul>
          <div class="button-row">
            <button class="read-more-btn" @click="toggleList('desexingWhy')">
              {{ expandedLists.desexingWhy ? 'Read Less' : 'Read More' }}
            </button>
          </div>
        </div>
        
        <div class="image-container clickable" @click="showDesexingDetails = !showDesexingDetails">
          <img src="https://th.bing.com/th/id/R.97aeacb01a86793d8e182c07d9741134?rik=RcLwWd0E5vrv8Q&riu=http%3a%2f%2fimg.mp.sohu.com%2fq_mini%2cc_zoom%2cw_640%2fupload%2f20170729%2fcd71841cb72a4f838203c618d57024ec_th.jpg&ehk=bzsiybnOi7GMl%2b%2f4l3COD1cFT%2fSHAAZk%2byOSoCjbmCc%3d&risl=&pid=ImgRaw&r=0" alt="Cat desexing">
          <p><em>Desexing is an important part of responsible pet ownership</em></p>
          <div class="image-overlay">
            <span>{{ showDesexingDetails ? 'Hide Details' : 'Click for More Details' }}</span>
          </div>
        </div>
      </div>
      
      <div v-if="showDesexingDetails" class="details-section">
        <h3>Desexing Details</h3>
        
        <div class="grid-2">
          <div class="info-card">
            <h4>How Desexing Works</h4>
            <p>Desexing is a safe and common procedure done by your local vet:</p>
            <ul class="checklist" v-if="!expandedLists.desexingHow">
              <li>For male cats, it stops them from fathering kittens</li>
              <li>For females, it prevents pregnancy completely</li>
            </ul>
            <ul class="checklist" v-else>
              <li>For male cats, it stops them from fathering kittens</li>
              <li>For females, it prevents pregnancy completely</li>
              <li>The surgery is quick, and most cats recover in just a few days</li>
              <li>Your vet will give you the best advice on timing and care</li>
            </ul>
            <button class="read-more-btn" @click="toggleList('desexingHow')">
              {{ expandedLists.desexingHow ? 'Read Less' : 'Read More' }}
            </button>
          </div>
          
          <div class="image-container">
            <img src="https://pic4.zhimg.com/v2-99b0dbe55b041ab7f28544ed5fe5804b_r.jpg" alt="Vet examining cat">
            <p><em>Veterinarians provide professional desexing services</em></p>
          </div>
        </div>
        
        <div class="grid-2">
          <div class="info-card">
            <h4>When to Desex Your Cat</h4>
            <p>It's important to plan desexing early to keep your cat healthy and meet local rules:</p>
            <ul class="checklist" v-if="!expandedLists.desexingWhen">
              <li>Vets often recommend desexing by around 4 to 5 months old</li>
              <li>Getting it done early helps avoid surprise pregnancies</li>
            </ul>
            <ul class="checklist" v-else>
              <li>Vets often recommend desexing by around 4 to 5 months old</li>
              <li>Getting it done early helps avoid surprise pregnancies</li>
              <li>Some councils have specific age requirements — check to stay on track</li>
              <li>Your vet will help you choose the right time based on your cat's health and lifestyle</li>
            </ul>
            <button class="read-more-btn" @click="toggleList('desexingWhen')">
              {{ expandedLists.desexingWhen ? 'Read Less' : 'Read More' }}
            </button>
          </div>
          
          <div class="image-container">
            <img src="https://pic4.zhimg.com/v2-2f42f6ef2db52093f21f9ef2ecdde44b_1200x500.jpg" alt="Kitten ready for desexing">
            <p><em>The ideal age for desexing is around 4-5 months</em></p>
          </div>
        </div>
      </div>
    </div>
    
    <div class="section">
      <h3>Microchipping Your Cat in Victoria</h3>
      
      <div class="grid-2">
        <div class="info-card">
          <h4>Why Microchipping Matters</h4>
          <p>Giving your cat a microchip is one of the best ways to help them find their way back home if they ever wander off:</p>
          <ul class="checklist" v-if="!expandedLists.microchipWhy">
            <li>Helps reunite lost cats with their owners quickly</li>
            <li>The chip stores your contact details in a secure registry</li>
            <li v-if="!isMobile">Mandatory for cats living in Victoria</li>
          </ul>
          <ul class="checklist" v-else>
            <li>Helps reunite lost cats with their owners quickly</li>
            <li>The chip stores your contact details in a secure registry</li>
            <li>Mandatory for cats living in Victoria</li>
            <li>Even if your cat stays indoors, accidents happen — microchipping gives peace of mind</li>
            <li>Be sure to keep your contact details up to date in the microchip database</li>
          </ul>
          <div class="button-row">
            <button class="read-more-btn" @click="toggleList('microchipWhy')">
              {{ expandedLists.microchipWhy ? 'Read Less' : 'Read More' }}
            </button>
          </div>
        </div>
        
        <div class="image-container clickable" @click="showMicrochipDetails = !showMicrochipDetails">
          <img src="https://fussiecat.com/wp-content/uploads/2019/05/Microchip-Your-Cat_Fussie-Cat-Blog-Article_web.jpg" alt="Cat microchipping">
          <p><em>Microchipping helps reunite lost cats with their owners</em></p>
          <div class="image-overlay">
            <span>{{ showMicrochipDetails ? 'Hide Details' : 'Click for More Details' }}</span>
          </div>
        </div>
      </div>
      
      <div v-if="showMicrochipDetails" class="details-section">
        <h3>Microchipping Details</h3>
        
        <div class="info-card">
          <h4>What Exactly Is a Microchip?</h4>
          <p>A microchip is a tiny device, about the size of a grain of rice, placed just under your cat's skin:</p>
          <ul class="checklist" v-if="!expandedLists.microchipWhat">
            <li>Each chip carries a special code unique to your cat</li>
            <li>Scanners used by vets and shelters can read the chip's number</li>
          </ul>
          <ul class="checklist" v-else>
            <li>Each chip carries a special code unique to your cat</li>
            <li>Scanners used by vets and shelters can read the chip's number</li>
            <li>Your contact information is linked to this code in a secure registry</li>
            <li>Keeping your details current ensures you can be contacted right away if your cat is found</li>
          </ul>
          <button class="read-more-btn" @click="toggleList('microchipWhat')">
            {{ expandedLists.microchipWhat ? 'Read Less' : 'Read More' }}
          </button>
          <p>It's a safe and quick process that gives your cat a permanent form of ID.</p>
        </div>
        
        <div class="info-card">
          <h4>When Should You Microchip Your Cat?</h4>
          <p>The best time to get your cat microchipped is early on:</p>
          <ul class="checklist" v-if="!expandedLists.microchipWhen">
            <li>Ideally, your cat should be microchipped before you bring them home</li>
            <li>If they aren't microchipped yet, book an appointment with your vet as soon as possible</li>
          </ul>
          <ul class="checklist" v-else>
            <li>Ideally, your cat should be microchipped before you bring them home</li>
            <li>If they aren't microchipped yet, book an appointment with your vet as soon as possible</li>
            <li>Some councils or animal rescue groups also offer microchipping services</li>
          </ul>
          <button class="read-more-btn" @click="toggleList('microchipWhen')">
            {{ expandedLists.microchipWhen ? 'Read Less' : 'Read More' }}
          </button>
          <p>Getting it done early means you'll always know your cat can be traced back to you if they get lost.</p>
        </div>
        
        <div class="info-card">
          <h4>Where Can You Get It Done?</h4>
          <p>Only trained professionals are allowed to microchip pets:</p>
          <ul class="checklist" v-if="!expandedLists.microchipWhere">
            <li>Local veterinarians offer microchipping services</li>
            <li>Animal shelters and welfare groups can also microchip cats</li>
          </ul>
          <ul class="checklist" v-else>
            <li>Local veterinarians offer microchipping services</li>
            <li>Animal shelters and welfare groups can also microchip cats</li>
            <li>Some local councils run special microchipping events</li>
          </ul>
          <button class="read-more-btn" @click="toggleList('microchipWhere')">
            {{ expandedLists.microchipWhere ? 'Read Less' : 'Read More' }}
          </button>
          <p>Check with your vet or community animal services to find the best option near you.</p>
        </div>
        
        <div class="info-card">
          <h4>Is It Painful for Your Cat?</h4>
          <p>Good news — it's quick and barely noticeable for your cat:</p>
          <ul class="checklist" v-if="!expandedLists.microchipPain">
            <li>The procedure only takes a few seconds</li>
            <li>Your cat might feel a tiny pinch, but it's over fast</li>
          </ul>
          <ul class="checklist" v-else>
            <li>The procedure only takes a few seconds</li>
            <li>Your cat might feel a tiny pinch, but it's over fast</li>
            <li>The short moment of discomfort is far outweighed by the safety it provides</li>
          </ul>
          <button class="read-more-btn" @click="toggleList('microchipPain')">
            {{ expandedLists.microchipPain ? 'Read Less' : 'Read More' }}
          </button>
          <p>Having your cat microchipped is one of the simplest ways to ensure they always have a way back to you.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DesexingMicrochipping',
  data() {
    return {
      showDesexingDetails: false,
      showMicrochipDetails: false,
      expandedLists: {
        desexingWhy: false,
        desexingHow: false,
        desexingWhen: false,
        microchipWhy: false,
        microchipWhat: false,
        microchipWhen: false,
        microchipWhere: false,
        microchipPain: false
      },
      isMobile: false
    }
  },
  mounted() {
    this.checkScreenSize();
    window.addEventListener('resize', this.checkScreenSize);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.checkScreenSize);
  },
  methods: {
    toggleList(list) {
      this.expandedLists[list] = !this.expandedLists[list];
    },
    expandAllLists() {
      Object.keys(this.expandedLists).forEach(key => {
        this.expandedLists[key] = true;
      });
    },
    collapseAllLists() {
      Object.keys(this.expandedLists).forEach(key => {
        this.expandedLists[key] = false;
      });
    },
    checkScreenSize() {
      this.isMobile = window.innerWidth <= 768;
    }
  }
}
</script>

<style scoped>
.desexing-microchipping {
  background-color: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  max-width: 1280px;
  margin: 0 auto;
}

.section {
  margin-bottom: 2rem;
}

.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  margin: 1.5rem 0;
}

.info-card {
  background-color: #f8f9fa;
  padding: 1.8rem;
  border-radius: 8px;
}

.details-section {
  margin: 2rem 0;
  background-color: #f8f9fa;
  padding: 2.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}

.image-container {
  text-align: center;
}

.clickable {
  cursor: pointer;
  position: relative;
  transition: all 0.3s ease;
}

.clickable:hover {
  transform: scale(1.02);
}

.image-overlay {
  position: absolute;
  bottom: 40px;
  left: 0;
  right: 0;
  background-color: rgba(44, 79, 70, 0.7);
  color: white;
  padding: 10px;
  border-radius: 0 0 8px 8px;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.clickable:hover .image-overlay {
  opacity: 1;
}

.image-container img {
  width: 100%;
  height: 320px;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.image-container p {
  margin-top: 0.5rem;
  color: #666;
  font-style: italic;
}

.checklist {
  list-style: none;
  margin: 1rem 0;
  padding-left: 0;
}

.checklist li {
  position: relative;
  padding-left: 1.5rem;
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
  margin-top: 1rem;
}

.btn:hover {
  background-color: #1a3a32;
  color: white !important;
}

.read-more-btn {
  background-color: transparent;
  color: var(--accent);
  border: 1px solid var(--accent);
  border-radius: 4px;
  padding: 0.4rem 1rem;
  margin-top: 0.8rem;
  margin-right: 1rem;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.read-more-btn:hover {
  background-color: var(--accent);
  color: white;
}

.button-row {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

@media (max-width: 768px) {
  .grid-2 {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .button-row {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .read-more-btn {
    margin-right: 0;
    margin-bottom: 0.8rem;
  }
  
  .image-overlay {
    opacity: 0.8; /* 在移动设备上始终显示提示 */
  }
}
</style> 