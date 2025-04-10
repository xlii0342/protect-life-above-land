const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  publicPath: '/static/',
  devServer: {
    port: 8080,
    open: true
  }
}) 