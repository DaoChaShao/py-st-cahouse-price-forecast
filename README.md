<p align="right">
  Language Switch / 语言选择：
  <a href="./README.zh-CN.md">🇨🇳 中文</a> | <a href="./README.md">🇬🇧 English</a>
</p>

**INTRODUCTION**
---
An interactive web application built with Streamlit that predicts median house values in California using a Linear
Regression model trained on the classic California Housing dataset.

**OVERVIEW**
---
This project demonstrates a classic machine learning workflow in a user-friendly web interface:

+ **Model:** A `scikit-learn` Linear Regression model.
+ **Data:** The famous [California Housing Prices](https://www.kaggle.com/datasets/camnugent/california-housing-prices)
  dataset.
+ **Frontend:** A beautiful and interactive UI built with `Streamlit`.
+ **Features:** Explore the dataset through dynamic visualisations and get instant price predictions by adjusting
  feature inputs.

**FEATURES**
---

+ **Exploratory Data Analysis (EDA):** Interactive maps and charts to explore the dataset.
+ **Real-time Prediction:** Adjust features like income, location, and house age to see predicted prices in real-time.
+ **Model Insights:** Understand which factors most influence the model's predictions.
+ **Web App:** No setup required! Run directly in your browser.

**WEB DEVELOPMENT**
---

1. Install NiceGUI with the command `pip install streamlit`.
2. Run the command `pip show streamlit` or `pip show streamlit | grep Version` to check whether the package has been
   installed and its version.

**PRIVACY NOTICE**
---
This application may require inputting personal information or private data to generate customised suggestions,
recommendations, and necessary results. However, please rest assured that the application does **NOT** collect, store,
or transmit your personal information. All processing occurs locally in the browser or runtime environment, and **NO**
data is sent to any external server or third-party service. The entire codebase is open and transparent — you are
welcome to review the code [here](./) at any time to verify how your data is handled.

**LICENCE**
---
This application is licensed under the [BSD-3-Clause License](LICENSE). You can click the link to read the licence.

**CHANGELOG**
---
This guide outlines the steps to automatically generate and maintain a project changelog using git-changelog.

1. Install the required dependencies with the command `pip install git-changelog`.
2. Run the command `pip show git-changelog` or `pip show git-changelog | grep Version` to check whether the changelog
   package has been installed and its version.
3. Prepare the configuration file of `pyproject.toml` at the root of the file.
4. The changelog style is [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
5. Run the command `git-changelog`, creating the `Changelog.md` file.
6. Add the file `Changelog.md` to version control with the command `git add Changelog.md` or using the UI interface.
7. Run the command `git-changelog --output CHANGELOG.md` committing the changes and updating the changelog.
8. Push the changes to the remote repository with the command `git push origin main` or using the UI interface.
