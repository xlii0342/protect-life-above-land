const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: '/',
  outputDir: '../vue_static',
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
          '^/api': ''  // 重写路径
        }
      }
    }
  }
})
