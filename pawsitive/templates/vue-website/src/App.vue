<template>
  <div id="app">
    <nav class="top-nav">
      <div class="logo">Pawsitive</div>
      <div class="nav-links">
        <router-link to="/">Home</router-link>
        <router-link to="/map">Map</router-link>
        <router-link to="/learn">Learn</router-link>
        <router-link to="/report">Report</router-link>
        <router-link to="/support">Support</router-link>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Inter', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.top-nav {
  background-color: #2f4f4f;
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
}

.logo::before {
  content: "🌿";
  font-size: 1.5rem;
  margin-right: 0.5rem;
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