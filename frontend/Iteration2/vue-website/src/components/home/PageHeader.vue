<template>
  <div class="page-header">
    <div class="header-video-background">
      <iframe 
        class="header-youtube-embed"
        :src="youtubeEmbedUrl"
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen
      ></iframe>
    </div>
    <div class="header-content">
      <h1>Feral Cats are Destroying Biodiversity</h1>
      <p>Discover the Impact of Feral Cats on Native Species</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PageHeader',
  props: {
    youtubeEmbedUrl: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>
/* 标题横幅样式 */
.page-header {
  width: 100%;
  text-align: center;
  padding: 0;
  position: relative;
  z-index: 2;
  margin-bottom: 3rem; 
  height: 500px; 
  overflow: hidden;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
}

.header-video-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  overflow: hidden;
}

.header-youtube-embed {
  width: 100vw;
  height: 56.25vw;
  min-height: 100%;
  min-width: 177.77vh;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
}

.header-content {
  position: relative;
  z-index: 1;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: linear-gradient(to bottom, rgba(0,0,0,0.1), rgba(47,79,79,0.8));
  padding: 3rem 2rem;
}

.page-header h1 {
  font-size: 4.2rem;
  margin-bottom: 1.5rem;
  font-weight: 800;
  letter-spacing: 1px;
  text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);
  color: white;
  animation: fadeInDown 1.2s ease-out;
  max-width: 90%;
}

.page-header p {
  font-size: 1.8rem;
  font-weight: 400;
  opacity: 0.95;
  color: white;
  max-width: 800px;
  margin: 0 auto;
  text-shadow: 1px 1px 6px rgba(0, 0, 0, 0.6);
  animation: fadeInUp 1.2s ease-out;
}

@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 响应式适配 */
@media (max-width: 1200px) {
  .page-header h1 {
    font-size: 3.5rem;
  }
}

@media (max-width: 992px) {
  .page-header {
    height: 450px;
  }
  
  .page-header h1 {
    font-size: 3rem;
  }
  
  .page-header p {
    font-size: 1.5rem;
  }
}

@media (max-width: 768px) {
  .page-header {
    height: 400px;
  }
  
  .page-header h1 {
    font-size: 2.5rem;
  }
  
  .page-header p {
    font-size: 1.3rem;
  }
}
</style> 