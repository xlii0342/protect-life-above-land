<template>
  <div class="app">
    <nav class="top-nav">
      <div class="logo" @click="goToHome">Pawsitive</div>
      <div
        class="hamburger"
        @click="toggleMenu"
        :class="{ active: isMenuOpen }"
      >
        <span></span>
        <span></span>
        <span></span>
      </div>
      <div class="nav-links" :class="{ active: isMenuOpen }">
        <router-link to="/" @click="closeMenu">Home</router-link>
        <router-link to="/learn" @click="closeMenu">Learn</router-link>
        <router-link to="/map" @click="closeMenu">Map</router-link>
        <router-link to="/report" @click="closeMenu">Report</router-link>
        <router-link to="/volunteer" @click="closeMenu">Support</router-link>
      </div>
      <div class="overlay" v-if="isMenuOpen" @click="closeMenu"></div>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      isMenuOpen: false,
    };
  },
  methods: {
    goToHome() {
      this.$router.push("/");
    },
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
    closeMenu() {
      this.isMenuOpen = false;
    },
  },
};
</script>

<style>
:root {
  --primary: #2f4f4f;
  --accent: #3a6659;
  --background: #f7f9f8;
  --text: #333;
  --accent-dark: #2c4f46;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Inter", sans-serif;
  background-color: var(--background);
  color: var(--text);
  line-height: 1.6;
}

.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

main {
  flex: 1;
}

.top-nav {
  background-color: var(--primary);
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  display: flex;
  align-items: center;
  cursor: pointer;
  transition: opacity 0.3s ease;
}

.logo::before {
  content: "🌿";
  font-size: 1.5rem;
  margin-right: 0.5rem;
}

.logo:hover {
  opacity: 0.8;
}

.hamburger {
  display: none;
  flex-direction: column;
  justify-content: space-between;
  width: 30px;
  height: 21px;
  cursor: pointer;
  z-index: 1010;
}

.hamburger span {
  display: block;
  height: 3px;
  width: 100%;
  background-color: white;
  border-radius: 3px;
  transition: all 0.3s ease;
}

/* 汉堡菜单动画 */
.hamburger.active span:nth-child(1) {
  transform: translateY(9px) rotate(45deg);
}

.hamburger.active span:nth-child(2) {
  opacity: 0;
}

.hamburger.active span:nth-child(3) {
  transform: translateY(-9px) rotate(-45deg);
}

.nav-links {
  display: flex;
  gap: 1.5rem;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-weight: 600;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  transition: background 0.3s ease;
}

.nav-links a:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.router-link-active {
  background-color: rgba(255, 255, 255, 0.1);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .hamburger {
    display: flex;
  }

  .nav-links {
    position: fixed;
    top: 0;
    right: -100%;
    width: 70%;
    height: 100vh;
    background-color: var(--primary);
    flex-direction: column;
    padding: 80px 0 30px;
    transition: all 0.4s ease;
    box-shadow: -5px 0 15px rgba(0, 0, 0, 0.1);
    z-index: 1002;
  }

  .nav-links.active {
    right: 0;
  }

  .nav-links a {
    margin: 0;
    padding: 15px 25px;
    width: 100%;
    border-radius: 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  }

  .nav-links a:hover {
    background-color: var(--accent-dark);
  }

  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1001;
    animation: fadeIn 0.3s ease;
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
}

@media (max-width: 480px) {
  .nav-links {
    width: 85%;
  }

  .logo {
    font-size: 1.3rem;
  }

  .top-nav {
    padding: 0.8rem 1.5rem;
  }
}
</style>
