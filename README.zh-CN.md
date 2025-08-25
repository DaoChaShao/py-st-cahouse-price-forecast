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

1. **数据管理**

+ 加载加州房价数据集 (`ca_house_prices.csv`)，并通过移除无关列（`latitude`, `longitude`, `ocean_proximity`）进行预处理。
+ 用户可以在只读交互式表格中浏览数据集。

2. **数据可视化**

+ 使用散点图可视化所选特征与房价之间的关系。

3. **单变量模型训练与预测**

+ 选择一个特征来训练 **线性回归模型** 进行房价预测。
+ 显示关键指标：
    - **均方误差 (MSE)**
    - **R² 系数**
+ 使用散点图可视化预测值与真实值的对比。
+ 用户可通过滑块选择特征值进行预测。
+ 系统会展示预测房价，并显示与数据集中真实值的差异。

4. **多变量模型训练与预测**

+ 选择多个特征来训练 **多变量线性回归模型**。
+ 显示指标：
    - **均方误差 (MSE)**
    - **R² 系数**
+ 使用散点图展示预测值与真实值的对比，用于模型评估。
+ 系统会为每个所选特征生成动态滑块，用户可交互式预测房价。

5. **基于 Session 的交互**

+ 使用 **Streamlit session_state** 管理：
    - 加载的数据集
    - 已选择的特征
    - 已训练的模型
    - 预测结果
+ 支持 **Home、Train、Predict** 页面之间的无缝交互。

6. **技术栈**

+ Python 3.12
+ Streamlit 负责界面交互
+ Pandas 进行数据处理
+ Scikit-learn 用于线性回归建模
+ 自定义工具类：计时器 (`Timer`) 和可视化绘图 (`plotly_scatter`)

**使用流程**
---

1. 在 **Home** 页面加载数据集。
2. 检查数据集，并可视化特征与房价的关系。
3. 训练 **单变量模型** 或 **多变量模型**。
4. 切换到 **Predict** 页面，通过滑块调整特征值，实时获取房价预测结果。

**快速开始**
---

1. 将本仓库克隆到本地计算机。
2. 使用以下命令安装所需依赖项：`pip install -r requirements.txt`
3. 使用以下命令运行应用程序：`streamlit run main.py`
4. 你也可以通过点击以下链接在线体验该应用：  
   [![Static Badge](https://img.shields.io/badge/Open%20in%20Streamlit-Daochashao-red?style=for-the-badge&logo=streamlit&labelColor=white)](https://ca-p-pre.streamlit.app/)

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
