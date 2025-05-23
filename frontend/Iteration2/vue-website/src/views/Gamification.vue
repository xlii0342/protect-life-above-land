<template>
  <div class="gamification-container">
    <!-- 左侧游戏背景描述 -->
    <div class="game-info-box left-info">
      <h3>🌏 Let's Play!</h3>
      <p>Animals need our help! Their homes are disappearing!</p>
      
      <div class="feature-section">
        <h4>🎵 Fun Stuff</h4>
        <p>Hear animal sounds and watch them move!</p>
      </div>
      
      <div class="why-matters">
        <h4>🧡 Help Them</h4>
        <p>Learn how to protect these amazing animals!</p>
      </div>
      
      <p class="hero-message">You can be a hero! 🐸🦜</p>
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
      <h3>🌟 How to Play</h3>
      <p>Glowing things can be clicked!</p>
      <p>Find ways to save each animal!</p>
      
      <div class="animal-info">
        <div class="animal-item">
          <h5>Growling Grass Frog</h5>
          <p>Breathes through skin!</p>
        </div>
        
        <div class="animal-item">
          <h5>Spot-tailed Quoll</h5>
          <p>Amazing tree climber!</p>
        </div>
        
        <div class="animal-item">
          <h5>Orange-bellied Parrot</h5>
          <p>Super rare bird!</p>
        </div>
        
        <div class="animal-item">
          <h5>Malleefowl</h5>
          <p>Builds huge nests!</p>
        </div>
      </div>
      
      <div class="join-rangers">
        <h4>Help the animals!</h4>
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
  font-family: 'Comic Sans MS', 'Bubblegum Sans', 'Nunito', 'Varela Round', sans-serif;
}

.game-info-box {
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.92);
  border-radius: 18px;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.12);
  max-width: 250px;
  overflow-y: auto;
  z-index: 10;
  margin: 10px;
  font-size: 1rem;
  line-height: 1.4;
  letter-spacing: 0.2px;
}

.game-info-box h3 {
  color: #2a7d2a;
  margin-top: 0;
  border-bottom: 3px solid #8bc34a;
  padding-bottom: 8px;
  font-size: 1.5rem;
  text-align: center;
  font-weight: 700;
}

.game-info-box h4 {
  color: #33691e;
  margin: 0 0 8px 0;
  font-size: 1.25rem;
  font-weight: 600;
}

.game-info-box p {
  margin-bottom: 12px;
  font-size: 1.05rem;
}

.left-info {
  left: 10px;
}

.right-info {
  right: 10px;
}

/* 新增样式 */
.feature-section, .why-matters {
  margin-top: 16px;
  padding: 12px;
  border-radius: 14px;
}

.feature-section {
  background-color: rgba(139, 195, 74, 0.15);
  border-left: 4px solid #8bc34a;
}

.why-matters {
  background-color: rgba(255, 152, 0, 0.15);
  border-left: 4px solid #ff9800;
}

.hero-message {
  margin-top: 20px;
  padding: 14px;
  background-color: rgba(76, 175, 80, 0.18);
  border-radius: 14px;
  text-align: center;
  font-weight: bold;
  color: #2e7d32;
  font-size: 1.2rem;
}

.animal-info {
  margin-top: 16px;
}

.animal-item {
  margin-bottom: 14px;
  padding: 12px;
  background-color: rgba(139, 195, 74, 0.15);
  border-left: 4px solid #8bc34a;
  border-radius: 12px;
}

.animal-item h5 {
  margin: 0 0 5px 0;
  color: #33691e;
  font-size: 1.15rem;
  font-weight: 600;
}

.animal-item p {
  margin: 0;
  font-style: italic;
  font-size: 1rem;
}

.join-rangers {
  margin-top: 18px;
  padding: 15px;
  background-color: rgba(255, 193, 7, 0.25);
  border-radius: 14px;
  text-align: center;
}

.join-rangers h4 {
  color: #ff6f00;
  margin-top: 0;
  font-size: 1.3rem;
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
    font-size: 0.95rem;
  }
  
  .game-info-box h3 {
    font-size: 1.4rem;
  }
  
  .game-info-box h4 {
    font-size: 1.2rem;
  }
  
  .animal-item h5 {
    font-size: 1.1rem;
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