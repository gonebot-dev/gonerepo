<div align="center">
  <a href="https://github.com/gonebot-dev">
    <img width="160" src="https://avatars.githubusercontent.com/u/179014534?s=200&v=4" />
  </a>

  <h1>GoneRepo</h1>
</div>
<div align="center">
    <p>✨ GoneBot 插件 & 适配器仓库 ✨</p>
</div>
<div align="center">
    <a href="https://github.com/gonebot-dev/gonerepo/actions"><img src="https://github.com/gonebot-dev/gonerepo/actions/workflows/ubuntu.yml/badge.svg" alt="Build Status"></a>
    <a href="https://github.com/tboox/tbox/blob/master/LICENSE.md">
      <img src="https://img.shields.io/github/license/gonebot-dev/gonerepo.svg?colorB=f48041&style=flat-square" alt="license" />
    </a>
</div>

## 简介 ([English](README.md))

GoneRepo 是一个插件和适配器仓库，用于 gonebot。它是一个插件和适配器的集合，可以用来扩展 gonebot 的功能。

## 提交你的适配器和插件！

如果你想要为 gonebot 提交适配器和插件，请按照以下步骤操作：

1. Fork 这个仓库
2. 创建一个新的分支
3. 做出你的更改
4. 提交你的更改
5. 将你的更改推送到你的分支

### 适配器
**对于适配器，你应当像这样编写你的 JSON 文件：**
```json
{
    "adapter": "onebotv11.OneBotV11",
    "description": "OneBotV11 adapter for gonebot. Use it for QQ.",
    "package": "github.com/gonebot-dev/goneadapter-onebotv11"
}
```
- **adapter**: 指定了你所定义的适配器实例
    如果配置顺利，gonebot 将会像这样使用你的适配器：
    ```go
    gonebot.LoadAdapter(&onebotv11.OneBotV11)
    ```
- **description**: 一段简短的描述，供用户阅读，你可以写任何你想要的内容，但最好不使用侮辱性词汇。
- **package**: 你的适配器的模块名称
    如果配置正确，gonebot 将会像这样安装你的适配器：
    ```go
    go get github.com/gonebot-dev/goneadapter-onebotv11
    ```
**你应当将你的 JSON 文件放在相应的位置，比如 `onebotv11` 在 `"packages/adapters/o/onebotv11/onebotv11.json"` 中**

### 插件
**对于插件，你应当像这样编写你的 JSON 文件：**
```json
{
    "plugin": "echo.Echo",
    "description": "Replys what you say",
    "package": "github.com/gonebot-dev/goneplugin-echo"
}
```
- **plugin**: 指定了你所定义的插件实例
    如果配置顺利，gonebot 将会像这样使用你的插件：
    ```go
    gonebot.LoadPlugin(&echo.Echo)
    ```
- **description**: 一段简短的描述，供用户阅读，你可以写任何你想要的内容，但最好不使用侮辱性词汇。
- **package**: 你的插件的模块名称
    如果配置正确，gonebot 将会像这样安装你的插件：
    ```go
    go get github.com/gonebot-dev/goneplugin-echo
    ```
**你应当将你的 JSON 文件放在相应的位置，比如 `echo` 在 `"packages/plugins/e/echo/echo.json"` 中**
