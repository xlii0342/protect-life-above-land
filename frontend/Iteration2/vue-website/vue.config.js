const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: '/',
  transpileDependencies: true,
  lintOnSave: false,
  devServer: {
    port: 8080,
    open: true
  }
})
