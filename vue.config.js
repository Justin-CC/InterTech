const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    host: 'localhost',
    port: 8080
  },
  lintOnSave: false,
  // devServer:{
  //   proxy:{
  //     '/api':{
  //       target:'',
  //       // pathReWrite: { '^/api': '' },
  //     },
  //   },
  // },
})
