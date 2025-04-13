<template>
  <div class="action-section">
    <h2>Let's Take Actions!</h2>
    
    <div class="actions">
      <!-- Learning 下拉按钮 -->
      <div class="dropdown">
        <div class="action-card">
          <button class="main-button learning-btn">
            <span class="btn-icon">🎓</span>
            <span class="btn-text">Learning</span>
            <span class="btn-arrow">▼</span>
          </button>
        </div>
        <div class="dropdown-content">
          <router-link to="/pet-owner" class="dropdown-item">
            <span class="item-icon">🐱</span>
            <span>Cat Owner</span>
          </router-link>
          <router-link to="/student-educator" class="dropdown-item">
            <span class="item-icon">📚</span>
            <span>Student/Educator</span>
          </router-link>
          <router-link to="/learn" class="dropdown-item">
            <span class="item-icon">🌱</span>
            <span>Beginner</span>
          </router-link>
        </div>
      </div>
      
      <!-- Report 按钮 -->
      <router-link to="/report" class="action-card">
        <button class="main-button report-btn">
          <span class="btn-icon">📝</span>
          <span class="btn-text">Report</span>
          <div class="btn-decoration"></div>
        </button>
      </router-link>
      
      <!-- Volunteer 按钮 -->
      <router-link to="/volunteer" class="action-card">
        <button class="main-button volunteer-btn">
          <span class="btn-icon">🤝</span>
          <span class="btn-text">Volunteer</span>
          <div class="btn-decoration"></div>
        </button>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ActionSection'
}
</script>

<style scoped>
/* 操作按钮区域样式 */
.action-section {
  margin-top: 2rem;
  padding: 2rem 1rem;
  position: relative;
}

.action-section h2 {
  color: #2f4f4f;
  font-size: 2.2rem;
  text-align: center;
  margin-bottom: 2.5rem;
  font-weight: 700;
  position: relative;
  display: inline-block;
  left: 50%;
  transform: translateX(-50%);
}

.action-section h2::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 25%;
  width: 50%;
  height: 3px;
  background: linear-gradient(90deg, transparent, #3a6659, transparent);
  border-radius: 10px;
}

/* 操作按钮样式统一 */
.actions {
  display: flex;
  justify-content: center;
  gap: 2.5rem;
  margin: 3rem 0;
}

/* 卡片式按钮容器 */
.action-card {
  position: relative;
  text-decoration: none;
  border-radius: 12px;
  transition: all 0.3s ease;
  overflow: hidden;
  background: white;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.08);
}

.action-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
}

/* 主按钮样式 */
.main-button {
  padding: 1.2rem 2rem;
  font-size: 1.1rem;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  color: white;
  font-weight: 600;
  letter-spacing: 0.5px;
  min-width: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
  z-index: 1;
}

.btn-icon {
  margin-right: 0.8rem;
  font-size: 1.3rem;
  transition: all 0.3s ease;
}

.btn-text {
  position: relative;
  z-index: 2;
}

.btn-arrow {
  font-size: 0.7rem;
  margin-left: 0.6rem;
  transition: transform 0.3s ease;
}

.dropdown:hover .btn-arrow {
  transform: rotate(180deg);
}

.btn-decoration {
  position: absolute;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.15);
  right: 15px;
  top: 50%;
  transform: translateY(-50%);
  transition: all 0.3s ease;
}

.main-button:hover .btn-decoration {
  transform: translateY(-50%) scale(1.5);
}

/* 按钮渐变背景色 */
.learning-btn {
  background: linear-gradient(135deg, #3a6659, #2c4f46);
  border-left: 4px solid #a3e4d7;
}

.learning-btn:hover {
  background: linear-gradient(135deg, #2c4f46, #1c3f36);
}

.report-btn {
  background: linear-gradient(135deg, #d35400, #ba4a00);
  border-left: 4px solid #f8c471;
}

.report-btn:hover {
  background: linear-gradient(135deg, #ba4a00, #a04000);
}

.volunteer-btn {
  background: linear-gradient(135deg, #4CAF50, #45a049);
  border-left: 4px solid #a3e4b5;
}

.volunteer-btn:hover {
  background: linear-gradient(135deg, #45a049, #3d8b3d);
}

/* 按钮悬停特效 */
.main-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.1);
  transition: all 0.4s ease;
  z-index: 0;
}

.main-button:hover::before {
  left: 100%;
}

/* 下拉菜单样式 */
.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  visibility: hidden;
  opacity: 0;
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  background-color: white;
  min-width: 200px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
  border-radius: 12px;
  z-index: 100;
  overflow: hidden;
  margin-top: 0.5rem;
  border: 1px solid rgba(58, 102, 89, 0.1);
  transition: all 0.3s ease;
}

.dropdown:hover .dropdown-content {
  visibility: visible;
  opacity: 1;
}

.dropdown-item {
  color: #333;
  padding: 1rem 1.5rem;
  text-decoration: none;
  display: flex;
  align-items: center;
  font-weight: 500;
  transition: all 0.2s ease;
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}

.item-icon {
  margin-right: 0.8rem;
  font-size: 1.1rem;
}

.dropdown-item:last-child {
  border-bottom: none;
}

.dropdown-item:hover {
  background: linear-gradient(to right, rgba(58, 102, 89, 0.1), transparent);
  color: #3a6659;
  padding-left: 2rem;
}

/* 响应式适配 */
@media (max-width: 768px) {
  .actions {
    flex-direction: column;
    align-items: center;
    gap: 2rem;
  }
  
  .action-card, .dropdown {
    width: 100%;
    max-width: 300px;
  }
  
  .main-button {
    width: 100%;
  }
  
  .dropdown-content {
    width: 100%;
  }
  
  .action-section h2 {
    font-size: 1.8rem;
  }
}
</style> 