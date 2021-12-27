ocp
===
===


配置环境
---
1. 安装node.js（官网下载，一键安装）
2. 安装依赖
    ```
        npm --registry https://registry.npm.taobao.org info underscore
    ```
3. 安装vue
   ```
       npm install --global vue
   ```
4. 安装vue-cli
    ```
        npm install --global vue-cli
        (输入vue检验是否安装成功）
    ```

运行
--

1. /app 文件夹下（ctrl+s实时显示更新）
    ``` bash
    # install dependencies
    npm install
    
    # serve with hot reload at localhost:8080
    npm run dev
    
    # build for production with minification
    npm run build
    
    # build for production and view the bundle analyzer report
    npm run build --report
    ```

    For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

2. /app.py 把pycharm的run configuration配成flask跑就行（要先build）

修改
---

App.vue是应用的入口，/src/components的几个相当于是不同的画挂在相框里（软工的啥模式来着）

src/router/index.js加入路由

然后在app.py里加入app.route+对应内容

冲鸭
===
2号答辩
25号预答辩
最好20号写好给丘那边
