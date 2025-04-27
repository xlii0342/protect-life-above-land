const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: '/static/',
  outputDir: '../vue_static',
  assetsDir: '',
  indexPath: 'index.html',
  filenameHashing: true,
  transpileDependencies: true,
  lintOnSave: false,
  devServer: {
    port: 8080,
    open: true
  }
})
