<template>
  <div class="gamification-container">
    <!-- 左侧游戏背景描述 -->
    <div class="game-info-box left-info">
      <h3>🌏 What's This Game About?</h3>
      <p>Some animals are in danger — their homes are disappearing!</p>
      <p>In this game, you'll learn where these animals live.</p>
      
      <div class="feature-section">
        <h4>🎵 Cool Features</h4>
        <p>Hear real animal sounds and see how they move!</p>
        <p>Each one has special actions you can watch.</p>
      </div>
      
      <div class="why-matters">
        <h4>🧡 Why It Matters</h4>
        <p>You'll discover how you can help protect these animals and their homes.</p>
      </div>
      
      <p class="hero-message">Be a hero — every little action counts! 🐸🦜</p>
    </div>
    
    <!-- 中间游戏框架 -->
    <div class="scratch-fullscreen">
      <iframe
        src="https://scratch.mit.edu/projects/1177756859/embed"
        allowtransparency="true"
        allow="fullscreen"
        allowfullscreen
        frameborder="0"
        scrolling="no"
      ></iframe>
    </div>
    
    <!-- 右侧游戏提示 -->
    <div class="game-info-box right-info">
      <h3>🌟 Game Tips!</h3>
      <p>Look for glowing things — they are clickable!</p>
      <p>Each habitat has a secret action to save an animal.</p>
      
      <div class="animal-info">
        <div class="animal-item">
          <h5>The Growling Grass Frog</h5>
          <p>Can breathe through its skin!</p>
        </div>
        
        <div class="animal-item">
          <h5>Spot-tailed Quoll</h5>
          <p>"They're expert tree climbers — and very shy."</p>
        </div>
        
        <div class="animal-item">
          <h5>Orange-bellied Parrot</h5>
          <p>"One of the rarest parrots in the world!"</p>
        </div>
        
        <div class="animal-item">
          <h5>Malleefowl</h5>
          <p>"Builds giant nests from leaves and dirt!"</p>
        </div>
      </div>
      
      <div class="join-rangers">
        <h4>Be the Hero! Help the animals!</h4>
      </div>
    </div>
  </div>
</template>

<script setup>
// nothing needed here
</script>

<style scoped>
.gamification-container {
  display: flex;
  position: fixed;
  top: 64px;
  left: 0;
  width: 100vw;
  height: calc(100vh - 64px);
  overflow: hidden;
}

.game-info-box {
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  max-width: 250px;
  overflow-y: auto;
  z-index: 10;
  margin: 10px;
}

.game-info-box h3 {
  color: #2a7d2a;
  margin-top: 0;
  border-bottom: 2px solid #8bc34a;
  padding-bottom: 8px;
}

.game-info-box h4 {
  color: #33691e;
  margin: 0 0 10px 0;
}

.left-info {
  left: 10px;
}

.right-info {
  right: 10px;
}

/* 新增样式 */
.feature-section, .why-matters {
  margin-top: 20px;
  padding: 10px;
  border-radius: 8px;
}

.feature-section {
  background-color: rgba(139, 195, 74, 0.1);
  border-left: 3px solid #8bc34a;
}

.why-matters {
  background-color: rgba(255, 152, 0, 0.1);
  border-left: 3px solid #ff9800;
}

.hero-message {
  margin-top: 20px;
  padding: 12px;
  background-color: rgba(76, 175, 80, 0.15);
  border-radius: 8px;
  text-align: center;
  font-weight: bold;
  color: #2e7d32;
  font-size: 1.1rem;
}

.animal-info {
  margin-top: 20px;
}

.animal-item {
  margin-bottom: 15px;
  padding: 10px;
  background-color: rgba(139, 195, 74, 0.1);
  border-left: 3px solid #8bc34a;
  border-radius: 4px;
}

.animal-item h5 {
  margin: 0 0 5px 0;
  color: #33691e;
}

.animal-item p {
  margin: 0;
  font-style: italic;
  font-size: 0.9rem;
}

.join-rangers {
  margin-top: 20px;
  padding: 15px;
  background-color: rgba(255, 193, 7, 0.2);
  border-radius: 8px;
  text-align: center;
}

.join-rangers h4 {
  color: #ff6f00;
  margin-top: 0;
}

.scratch-fullscreen {
  flex: 1;
  position: relative;
  height: 100%;
}

.scratch-fullscreen iframe {
  position: absolute;
  top: -40px;
  left: 0;
  width: 100%;
  height: calc(100% + 40px);
  border: none;
}

ul {
  padding-left: 20px;
}

/* 响应式设计 */
@media (max-width: 1200px) {
  .game-info-box {
    max-width: 200px;
    font-size: 0.9rem;
  }
}

@media (max-width: 992px) {
  .gamification-container {
    flex-direction: column;
    align-items: center;
  }
  
  .game-info-box {
    position: static;
    max-width: 90%;
    margin: 10px auto;
  }
  
  .scratch-fullscreen {
    width: 100%;
    height: 60%;
  }
  
  .left-info, .right-info {
    height: auto;
    max-height: 20vh;
  }
}
</style>