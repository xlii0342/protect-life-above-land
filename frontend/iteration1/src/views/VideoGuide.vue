<template>
  <div class="video-guide">
    <div class="home-icon" @click="navigateTo('/home')" title="Go to Home Page">
      🏠
    </div>
    
    <div class="video-container">
      <iframe 
        class="youtube-embed"
        :src="youtubeEmbedUrl"
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen
      ></iframe>
      
      <div class="content-overlay with-youtube">
        <h1></h1>
        <p>Learn about Australian wildlife conservation and endangered species, and explore ways for humans and nature to coexist harmoniously</p>
        
        <button class="start-exploring" @click="navigateTo('/home')">Explore Conservation</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoGuide',
  data() {
    return {
      youtubeVideoId: 'WnWm-zy5qKE' // 从用户提供的嵌入代码中提取的正确YouTube视频ID
    }
  },
  computed: {
    youtubeEmbedUrl() {
      return `https://www.youtube.com/embed/${this.youtubeVideoId}?autoplay=1&mute=1&loop=1&playlist=${this.youtubeVideoId}&controls=0&showinfo=0&rel=0&modestbranding=1&iv_load_policy=3`
    }
  },
  methods: {
    navigateTo(path) {
      this.$router.push(path)
    }
  }
}
</script>

<style scoped>
/* 为VideoGuide页面隐藏导航栏，创建沉浸式体验 */
:deep(.top-nav) {
  display: none;
}

/* 确保页面占满整个视口 */
.video-guide {
  min-height: 100vh;
  width: 100%;
  overflow: hidden;
  position: relative;
}

.video-container {
  width: 100%;
  height: 100vh;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #000;
  background-image: linear-gradient(to top, rgba(0,0,0,0.3) 0%, transparent 50%);
}

.youtube-embed {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
}

.content-overlay {
  position: relative;
  z-index: 2;
  text-align: center;
  padding: 2.5rem;
  background-color: rgba(0, 0, 0, 0.1);
  border-radius: 0;
  color: white;
  max-width: 1000px;
  width: 90%;
  box-shadow: none;
  border: none;
  animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.content-overlay.with-youtube {
  background-color: transparent;
}

.content-overlay h1 {
  font-size: 4rem;
  margin-bottom: 1.5rem;
  text-shadow: none;
  font-weight: 700;
  letter-spacing: 1px;
}

.content-overlay p {
  font-size: 1.6rem;
  margin-bottom: 3rem;
  line-height: 1.6;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
  text-shadow: none;
  font-weight: 400;
}

.start-exploring {
  background-color: var(--accent);
  color: white;
  border: 2px solid white;
  padding: 1.2rem 3rem;
  font-size: 1.5rem;
  border-radius: 3rem;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 3rem;
  box-shadow: none;
  font-weight: 600;
  letter-spacing: 1px;
  text-shadow: none;
  /* 使用半透明背景 */
  background-color: rgba(58, 102, 89, 0.7);
}

.start-exploring:hover {
  background-color: var(--accent);
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.start-exploring:active {
  transform: translateY(0);
  box-shadow: none;
}

/* 添加Home图标样式 */
.home-icon {
  position: fixed;
  top: 20px;
  right: 20px;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: rgba(47, 79, 79, 0.7);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  cursor: pointer;
  z-index: 100;
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.home-icon:hover {
  background-color: var(--accent);
  transform: scale(1.1);
}

@media (max-width: 768px) {
  .content-overlay h1 {
    font-size: 2.6rem;
  }
  
  .content-overlay p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
  }
  
  .content-overlay {
    padding: 2rem 1.5rem;
    width: 95%;
  }
  
  .start-exploring {
    padding: 1rem 2.5rem;
    font-size: 1.3rem;
  }
}

@media (max-width: 480px) {
  .content-overlay h1 {
    font-size: 2.2rem;
  }
  
  .content-overlay p {
    font-size: 1.1rem;
  }
  
  .start-exploring {
    padding: 0.8rem 2rem;
    font-size: 1.2rem;
  }
}
</style> 