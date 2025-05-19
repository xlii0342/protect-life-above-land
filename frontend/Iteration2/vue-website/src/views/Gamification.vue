<template>
  <div class="scratch-fullscreen">
    <iframe
      src="https://scratch.mit.edu/projects/1176956189/embed"
      allowtransparency="true"
      allow="fullscreen"
      allowfullscreen
      frameborder="0"
      scrolling="no"
    ></iframe>
  </div>
</template>

<script setup>
// nothing needed here
</script>

<style scoped>
.scratch-fullscreen {
  position: fixed;
  top: 64px;                      
  left: 0;
  width: 100vw;
  height: calc(100vh - 64px);     
  overflow: hidden;
  z-index: 0;                      
}

.scratch-fullscreen iframe {
  position: absolute;
  top: -40px;                     
  left: 0;
  width: 100vw;
  height: calc(100vh - 64px + 40px);
  border: none;
}
</style>
