<template>
  <div class="app">
    <nav class="top-nav">
      <div class="logo" @click="goToHome">Pawsitive</div>
      <div class="nav-links">
        <router-link to="/home">Home</router-link>
        <router-link to="/learn">Learn</router-link>
        <router-link to="/map">Map</router-link>
        <router-link to="/report">Report</router-link>
        <router-link to="/support">Support</router-link>
      </div>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  methods: {
    goToHome() {
      this.$router.push('/');
    }
  }
}
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
  font-family: 'Inter', sans-serif;
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
</style> 