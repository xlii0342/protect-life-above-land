<template>
  <div class="learn-page">
    <section class="container">
      <h1>Learning Resource Center</h1>
      <p>Explore our carefully curated educational resources to learn how to protect local ecosystems and address the threat of feral cats. Whether you're a student, teacher, or enthusiastic community member, we have content suited for you.</p>

      <h2>Understanding the Feral Cat Threat</h2>

      <div class="video-section">
        <h3>Educational Video</h3>
        <div class="video-container">
          <iframe width="560" height="315" src="https://www.youtube.com/embed/h6DYmM1lYvs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </div>
      </div>

      <div class="grid-2">
        <div class="card">
          <h3>🔬 Feral Cat Impact on Biodiversity</h3>
          <p>Feral cats are one of the most serious threats to Australia's biodiversity. Since European settlers brought domestic cats, they have become an invasive species, killing over 2 billion native animals annually.</p>
          <p>In Victoria, feral cats have led to numerous native species becoming endangered or extinct, disrupting the balance of local ecosystems. They not only directly prey on small mammals, birds, and reptiles, but also indirectly affect wildlife populations through disease transmission.</p>
        </div>
        <div class="card">
          <h3>📊 Key Data and Research</h3>
          <p>According to recent research, a single feral cat can kill up to 740 native animals per year. In some areas of Victoria, feral cat density reaches 5-10 cats per square kilometer.</p>
          <p>Our research team monitors feral cat activity through radio tracking and camera traps, discovering they particularly prefer forest edges and shrubland areas, which are often habitats for many endangered species.</p>
        </div>
      </div>

      


    </section>
    <Footer />
  </div>
</template>

<script>
import Footer from '@/components/Footer.vue'

export default {
  name: 'Learn',
  components: {
    Footer
  }
}
</script>

<style scoped>
.learn-page {
  padding: 2rem 0;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  flex: 1;
}

h1 {
  color: var(--primary);
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

h2 {
  color: var(--primary);
  margin: 2rem 0 1rem;
  font-size: 2rem;
}

h3 {
  color: var(--primary);
  margin-bottom: 1rem;
  font-size: 1.25rem;
}

p {
  color: var(--text);
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.grid-2 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}

.card {
  background: var(--background);
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
}

.accent-link {
  color: var(--accent);
  font-weight: bold;
  text-decoration: none;
  transition: color 0.3s ease;
}

.accent-link:hover {
  color: var(--accent-dark);
}

.video-section {
  margin: 3rem 0;
  padding: 2rem;
  background: white;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

.video-section h3 {
  color: var(--primary);
  margin-bottom: 1.5rem;
  text-align: center;
  font-size: 1.8rem;
}

.video-container {
  position: relative;
  width: 100%;
  padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
  height: 0;
  overflow: hidden;
  border-radius: 8px;
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 8px;
}

@media (max-width: 768px) {
  .grid-2 {
    grid-template-columns: 1fr;
  }
  
  .container {
    padding: 0 1rem;
  }

  .video-section {
    padding: 1rem;
    margin: 2rem 0;
  }
  
  .video-section h3 {
    font-size: 1.5rem;
  }
}
</style> 