<template>
  <div class="best-practices">
    <h2>Best Practices for Responsible Cat Ownership</h2>
    
    <div class="grid-2">
      <div>
        <h3>Why Indoor Cats Matter?</h3>
        <p>In Australia, outdoor domestic cats kill over 390 million wild animals annually, including birds, reptiles, and small mammals. By keeping your cat indoors or in controlled environments, you can:</p>
        <ul class="checklist">
          <li>Protect wildlife from predation</li>
          <li>Reduce your cat's risk of traffic accidents</li>
          <li>Prevent your cat from contracting diseases</li>
          <li>Avoid conflicts with neighbors</li>
        </ul>
      </div>
      
      <div class="image-container">
        <img src="https://picx.zhimg.com/v2-619596c5f3da6d65061098f798478361_r.jpg?source=1def8aca" alt="Indoor cat" width="350" style="max-width: 100%; height: auto;">
        <p><em>Indoor cats can live safe, healthy lives</em></p>
      </div>
    </div>
    
    <h3>Cat Care Checklist</h3>
    <div class="grid-3">
      <div class="card">
        <h3>💉 Health Care</h3>
        <ul class="checklist">
          <li>Spay/neuter your cat</li>
          <li>Keep vaccinations up to date</li>
          <li>Microchip and register with local council</li>
          <li>Annual veterinary check-ups</li>
        </ul>
      </div>
      
      <div class="card">
        <h3>🏠 Environmental Enrichment</h3>
        <ul class="checklist">
          <li>Provide climbing and resting areas</li>
          <li>Offer a variety of toys and games</li>
          <li>Create window viewing stations</li>
          <li>Install scratching posts</li>
        </ul>
      </div>
      
      <div class="card">
        <h3>🌿 Outdoor Management</h3>
        <ul class="checklist">
          <li>Use secure cat fencing</li>
          <li>Train your cat to walk on a harness</li>
          <li>Provide safe outdoor spaces</li>
          <li>Consider GPS tracking devices</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BestPractices'
}
</script>

<style scoped>
.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  margin: 1rem 0;
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
  line-height: 1.4;
}

.checklist {
  list-style: none;
  margin: 0.5rem 0;
  padding-left: 0;
}

.checklist li {
  position: relative;
  padding-left: 1.5rem;
  margin-bottom: 0.4rem;
  line-height: 1.4;
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
  margin: 1rem 0;
}

.image-container img {
  max-width: 100%;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  margin-bottom: 0.3rem;
}

.image-container p {
  color: #666;
  font-style: italic;
  margin-top: 0.3rem;
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .grid-2 {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
}
</style> 