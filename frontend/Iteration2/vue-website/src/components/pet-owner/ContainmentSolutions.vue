<template>
  <div class="containment-solutions">
    <h2>Cat Containment Solutions</h2>
    
    <p>There are several ways to create safe outdoor spaces for your cat that protect wildlife:</p>
    
    <div class="solutions-grid">
      <div class="card" style="max-width: 400px; cursor: pointer;" @click="showDIYModal = true">
        <h3>DIY Cat Fencing</h3>
        <div class="image-wrapper">
          <img src="https://i.pinimg.com/originals/90/65/7f/90657f208ae0f4f96c98748548d804cd.jpg" alt="DIY Cat Fencing Example">
        </div>
        <p v-if="!expandedCards.diy">Build your own outdoor enclosure using mesh panels or netting to create a safe space for your cat.</p>
        <p v-else>Build your own outdoor enclosure using mesh panels or netting to create a safe space for your cat. These setups are perfect for backyards and can be customised to fit any size area.</p>
        <div class="button-container">
          <button class="read-more-btn" @click.stop="toggleCard('diy')">
            {{ expandedCards.diy ? 'Read Less' : 'Read More' }}
          </button>
          <p class="click-hint">Click for detailed guide</p>
        </div>
      </div>
      
      <div class="card" style="max-width: 400px;">
        <h3>Supervised Outdoor Time on a Leash</h3>
        <div class="image-wrapper">
          <img src="https://imgix.bustle.com/uploads/image/2019/9/13/76f33333-2481-4f27-9680-119791acd5db-best-cat-harnesses.jpg" alt="Cat on a leash">
        </div>
        <p v-if="!expandedCards.leash">Training your cat to walk on a harness and leash gives them safe outdoor experiences under your watchful eye.</p>
        <p v-else>Training your cat to walk on a harness and leash gives them safe outdoor experiences under your watchful eye. While it takes a little practice, it's a fun way for your cat to explore while staying close to you.</p>
        <button class="read-more-btn" @click="toggleCard('leash')">
          {{ expandedCards.leash ? 'Read Less' : 'Read More' }}
        </button>
      </div>
      
      <div class="card" style="max-width: 400px;">
        <h3>Catios (Cat Patios)</h3>
        <div class="image-wrapper">
          <img src="https://i.pinimg.com/originals/77/f2/80/77f280a83466d597d92441ceae397201.jpg" alt="Catio example">
        </div>
        <p v-if="!expandedCards.catios">Catios are purpose-built enclosures that attach to your house or stand alone in your yard. They give your cat a taste of the outdoors while keeping them secure.</p>
        <p v-else>Catios are purpose-built enclosures that attach to your house or stand alone in your yard. They give your cat a taste of the outdoors while keeping them secure. With climbing shelves, tunnels, and cosy spots, catios are like mini playgrounds for your cat — safe for them, and safe for native wildlife too.</p>
        <button class="read-more-btn" @click="toggleCard('catios')">
          {{ expandedCards.catios ? 'Read Less' : 'Read More' }}
        </button>
      </div>
      
      <div class="card" style="max-width: 400px;">
        <h3>Portable Outdoor Playpens</h3>
        <div class="image-wrapper">
          <img src="https://bestpetpro.com/wp-content/uploads/2020/05/2.-Outback-Jack-Outdoor-Cat-Enclosures-for-Indoor-Cats-768x512.jpg" alt="Portable cat playpen">
        </div>
        <p v-if="!expandedCards.playpen">For flexibility, pop-up playpens are a great choice. Lightweight and easy to move, they let your cat enjoy outdoor time at home, in the park, or even when visiting friends.</p>
        <p v-else>For flexibility, pop-up playpens are a great choice. Lightweight and easy to move, they let your cat enjoy outdoor time at home, in the park, or even when visiting friends. They're perfect for short outdoor sessions and easy to pack away when not in use.</p>
        <button class="read-more-btn" @click="toggleCard('playpen')">
          {{ expandedCards.playpen ? 'Read Less' : 'Read More' }}
        </button>
      </div>
    </div>

    <div class="center-btn">
      <button class="read-more-btn expand-all" @click="toggleAllCards">
        {{ allCardsExpanded ? 'Collapse All' : 'Expand All' }}
      </button>
    </div>

    <!-- DIY Cat Fencing Modal -->
    <div v-if="showDIYModal" class="modal-overlay" @click="showDIYModal = false">
      <div class="modal-content" @click.stop>
        <span class="close-button" @click="showDIYModal = false">&times;</span>
        <h2 style="color: var(--primary); margin-bottom: 20px;">DIY Cat Fencing Detailed Guide</h2>
        
        <div style="margin-bottom: 30px;">
          <h3 style="color: var(--accent);">Materials Needed</h3>
          <ul class="checklist">
            <li>Nylon or metal mesh (at least 1.8m wide)</li>
            <li>PVC pipes (around 2cm in diameter, length depends on your fence perimeter)</li>
            <li>Cable ties or S-hooks</li>
            <li>Scissors and measuring tape</li>
            <li>Gloves (to prevent cuts)</li>
          </ul>
        </div>
        
        <div style="margin-bottom: 30px;">
          <h3 style="color: var(--accent);">Step-by-Step Instructions</h3>
          <ol style="padding-left: 20px; line-height: 1.8;">
            <li><strong>Measure the fence:</strong> Determine the perimeter of the area where you want to install the cat fence.</li>
            <li><strong>Prepare the mesh:</strong> Cut the nylon mesh to a width of at least 1.8m and length equal to your fence perimeter plus 30cm for overlap.</li>
            <li><strong>Prepare PVC pipes:</strong> Cut the PVC pipes into 60-80cm segments.</li>
            <li><strong>Bend the PVC pipes:</strong> Bend the PVC pipes at a 45-degree angle to create the inward-facing barrier.</li>
            <li><strong>Install the brackets:</strong> Attach the bent PVC pipes to the top of your existing fence at 1-1.5m intervals.</li>
            <li><strong>Install the mesh:</strong> Pull the mesh over the PVC pipe brackets, ensuring it folds inward from the top of the fence.</li>
            <li><strong>Secure the mesh:</strong> Use cable ties to secure the mesh to both the fence and PVC pipes.</li>
            <li><strong>Inspect:</strong> Check for any holes or loose areas where cats might be able to escape.</li>
          </ol>
        </div>
        
        <div style="margin-bottom: 30px;">
          <h3 style="color: var(--accent);">Maintenance Tips</h3>
          <ul class="checklist">
            <li>Regularly check the fence for any damage or loose sections</li>
            <li>Pay special attention after strong winds or heavy rain</li>
            <li>If using nylon mesh, consider replacing it every 1-2 years as sunlight can degrade the material</li>
          </ul>
        </div>
        
        <div>
          <p style="color: var(--primary); font-weight: bold;">Safety Considerations</p>
          <p>Ensure the installation is secure to prevent cats from escaping or getting injured. For particularly active or skilled climbing cats, additional safety measures may be necessary.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContainmentSolutions',
  data() {
    return {
      showDIYModal: false,
      expandedCards: {
        diy: false,
        leash: false,
        catios: false,
        playpen: false
      }
    }
  },
  computed: {
    allCardsExpanded() {
      return Object.values(this.expandedCards).every(value => value === true);
    }
  },
  methods: {
    toggleCard(card) {
      this.expandedCards[card] = !this.expandedCards[card];
    },
    toggleAllCards() {
      const newValue = !this.allCardsExpanded;
      Object.keys(this.expandedCards).forEach(card => {
        this.expandedCards[card] = newValue;
      });
    }
  }
}
</script>

<style scoped>
.containment-solutions {
  padding: 1rem;
}

.solutions-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2rem;
  margin: 2rem 0;
}

.card {
  background: white;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  width: 100%;
  margin: 0 auto;
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

.image-wrapper {
  width: 90%;
  height: 220px;
  overflow: hidden;
  border-radius: 8px;
  margin: 1rem auto;
}

.image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.image-wrapper:hover img {
  transform: scale(1.05);
}

.click-hint {
  color: var(--accent);
  margin-top: auto;
  text-align: center;
  font-size: 0.9em;
  font-style: italic;
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

.read-more-btn {
  background-color: transparent;
  color: var(--accent);
  border: 1px solid var(--accent);
  border-radius: 4px;
  padding: 0.4rem 1rem;
  margin-top: 0.8rem;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.3s ease;
  align-self: flex-start;
}

.read-more-btn:hover {
  background-color: var(--accent);
  color: white;
}

.expand-all {
  background-color: var(--accent);
  color: white;
  font-weight: 600;
  padding: 0.5rem 1.5rem;
}

.expand-all:hover {
  background-color: var(--accent-dark);
}

.center-btn {
  text-align: center;
  margin: 2rem 0 1rem;
}

.button-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: auto;
}

@media (max-width: 768px) {
  .solutions-grid {
    justify-content: center;
  }
  
  .card {
    max-width: 90% !important;
  }
  
  .modal-content {
    width: 95%;
    margin: 2% auto;
    padding: 1.5rem;
  }
}
</style> 