<p align="right">
  Language Switch / 语言选择：
  <a href="./README.zh-CN.md">🇨🇳 中文</a> | <a href="./README.md">🇬🇧 English</a>
</p>

**应用简介**
---
一个使用 Streamlit 构建的交互式网络应用程序，它通过基于经典加州房价数据集训练的线性回归模型，来预测加利福尼亚州的房屋中位价。

**项目概览**
---
本项目在一个用户友好的Web界面中，完整演示了经典的机器学习工作流程：

+ **模型：** 使用 `scikit-learn` 的线性回归模型。
+ **数据：** 著名的 [加州房价](https://www.kaggle.com/datasets/camnugent/california-housing-prices) 数据集。
+ **前端：** 使用 `Streamlit` 构建的美观且交互式的用户界面。
+ **功能：** 通过动态可视化图表探索数据集，并通过调整特征输入来获取即时价格预测。

**应用特色**
---

+ **数据探索分析 (EDA):** 通过交互式地图和图表探索数据集分布。
+ **实时预测:** 调整收入、地理位置、房屋年龄等特征，实时查看预测价格。
+ **模型解读:** 了解哪些因素是模型预测价格的关键依据。
+ **Web应用:** 无需任何环境配置！直接在浏览器中运行。

**网页开发**
---

1. 使用命令`pip install streamlit`安装`Streamlit`平台。
2. 执行`pip show streamlit`或者`pip show git-streamlit | grep Version`检查是否已正确安装该包及其版本。

**隐私声明**
---
本应用可能需要您输入个人信息或隐私数据，以生成定制建议和结果。但请放心，应用程序 **不会**
收集、存储或传输您的任何个人信息。所有计算和数据处理均在本地浏览器或运行环境中完成，**不会** 向任何外部服务器或第三方服务发送数据。

整个代码库是开放透明的，您可以随时查看 [这里](./) 的代码，以验证您的数据处理方式。

**许可协议**
---
本应用基于 **BSD-3-Clause 许可证** 开源发布。您可以点击链接阅读完整协议内容：👉 [BSD-3-Clause License](./LICENSE)。

**更新日志**
---
本指南概述了如何使用 git-changelog 自动生成并维护项目的变更日志的步骤。

1. 使用命令`pip install git-changelog`安装所需依赖项。
2. 执行`pip show git-changelog`或者`pip show git-changelog | grep Version`检查是否已正确安装该包及其版本。
3. 在项目根目录下准备`pyproject.toml`配置文件。
4. 更新日志遵循 [Conventional Commits](https://www.conventionalcommits.org/zh-hans/v1.0.0/) 提交规范。
5. 执行命令`git-changelog`创建`Changelog.md`文件。
6. 使用`git add Changelog.md`或图形界面将该文件添加到版本控制中。
7. 执行`git-changelog --output CHANGELOG.md`提交变更并更新日志。
8. 使用`git push origin main`或 UI 工具将变更推送至远程仓库。
