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
    
    <!-- 简化后的说明和按钮，只做外部跳转 -->
    <div
      style="background-color: #f5f5f5; padding: 1rem; border-radius: 8px; margin-top: 2rem; border-left: 4px solid var(--primary);"
    >
      <h3>Find Regulations for Your Area</h3>
      <p>
        Cat management regulations may vary between municipalities.  
        Click the button below to view the official “Know your council” page.
      </p>
      <button
        @click="goToCouncilPage"
        class="btn"
        style="margin-top: 1rem;"
      >
        Find My Local Council
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Regulations',
  methods: {
    goToCouncilPage() {
      window.location.href = 'https://www.vic.gov.au/know-your-council'
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
}

.card {
  background: white;
  border-radius: 10px;
  padding: 1rem;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}

.card h3 {
  color: var(--primary);
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
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 5px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color .3s;
}

.btn:hover {
  background-color: #1a3a32;
}

@media (max-width: 768px) {
  .grid-2 {
    grid-template-columns: 1fr;
  }
}
</style>
