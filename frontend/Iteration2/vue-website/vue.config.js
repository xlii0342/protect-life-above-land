// vue-website/vue.config.js
const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
 
  publicPath: '/static/',

  outputDir: 'dist',

 
  assetsDir: '',

  
  indexPath: 'index.html',

  
  filenameHashing: true,

  
  transpileDependencies: true,

  
  lintOnSave: false,


  devServer: {
    port: 8080,
    open: true,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        pathRewrite: {
          '^/api': '' 
        }
      }
    }
  }
})
