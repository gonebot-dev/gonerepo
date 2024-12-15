<div align="center">
  <a href="https://github.com/gonebot-dev">
	<img width="160" src="https://avatars.githubusercontent.com/u/179014534?s=200&v=4" />
  </a>

  <h1>GoneRepo</h1>
</div>
<div align="center">
	<p>✨ Plugin & Adapter repository for gonebot ✨</p>
</div>
<div align="center">
    <a href="https://github.com/gonebot-dev/gonerepo/actions"><img src="https://github.com/gonebot-dev/gonerepo/actions/workflows/ubuntu.yml/badge.svg" alt="Build Status"></a>
	<a href="https://github.com/tboox/tbox/blob/master/LICENSE.md">
	  <img src="https://img.shields.io/github/license/gonebot-dev/gonerepo.svg?colorB=f48041&style=flat-square" alt="license" />
	</a>
</div>

## Introduction ([中文](README_zh.md))

GoneRepo is a plugin and adapter repository for gonebot. It is a collection of plugins and adapters that can be used to extend the functionality of gonebot.

## Submit your own plugins & adapters!

If you want to contribute to this project, please follow these steps:

1. Fork this repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push your changes to your fork

### Adapter
**For adapters, you should write your json like this:**
```json
{
    "adapter": "onebotv11.OneBotV11",
    "description": "OneBotV11 adapter for gonebot. Use it for QQ.",
    "package": "github.com/gonebot-dev/goneadapter-onebotv11"
}
```
- **adapter**: The adapter instance for gonebot to use.
    If correct, gonebot will use your adapter like this:
    ```go
    gonebot.LoadAdapter(&onebotv11.OneBotV11)
    ```
- **description**: A short description of the adapter for users to read, you can write anything you want, but it's better not to use offensive words.
- **package**: The module name of your adapter.
    If correct, gonebot will install your adapter like this:
    ```go
    go get github.com/gonebot-dev/goneadapter-onebotv11
    ```
**You should put your json file correspondingly, like `onebotv11` in `"packages/adapters/o/onebotv11/onebotv11.json"`**

### Plugin
**For plugins, you should write your json like this:**
```json
{
    "plugin": "echo.Echo",
    "description": "Replys what you say",
    "package": "github.com/gonebot-dev/goneplugin-echo"
}
```

- **plugin**: The plugin instance for gonebot to use.
    If correct, gonebot will use your plugin like this:
    ```go
    gonebot.LoadPlugin(&echo.Echo)
    ```
- **description**: A short description of the plugin for users to read, you can write anything you want, but it's better not to use offensive words.
- **package**: The module name of your plugin.
    If correct, gonebot will install your plugin like this:
    ```go
    go get github.com/gonebot-dev/goneplugin-echo
    ```
**You should put your json file correspondingly, like `echo` in `"packages/plugins/e/echo/echo.json"`**
