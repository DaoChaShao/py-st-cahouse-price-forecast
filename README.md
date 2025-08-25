<p align="right">
  Language Switch / 语言选择：
  <a href="./README.zh-CN.md">🇨🇳 中文</a> | <a href="./README.md">🇬🇧 English</a>
</p>

**INTRODUCTION**
---

**California House Price Forecast** is an interactive Streamlit application designed for exploring, visualising,
training, and predicting house prices in California using both single-variable and multi-variable linear regression
models.

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

1. **Data Management**

+ Load the California housing dataset (`ca_house_prices.csv`) and preprocess it by removing irrelevant columns (
  `latitude`, `longitude`, `ocean_proximity`).
+ Users can browse the dataset in a read-only interactive table.

2. **Data Visualisation**

+ Visualise relationships between selected features and house prices using scatter charts.

3. **Single-Variable Model Training & Prediction**

+ Select one feature to train a **linear regression model** to predict house prices.
+ Displays key metrics:
    - **Mean Squared Error (MSE)**
    - **R² Score**
+ Visualises predicted vs actual house prices with scatter charts.
+ Allows users to select a feature value via a slider to make predictions.
+ Users can see the predicted house price along with the difference from the original value in the dataset.

4. **Multi-Variable Model Training & Prediction**

+ Select multiple features to train a **multi-variable linear regression model**.
+ Displays metrics:
    - **Mean Squared Error (MSE)**
    - **R² Score**
+ Scatter chart shows predicted vs actual house prices for evaluation.
+ Use dynamic sliders for each selected feature to predict house prices interactively.

5. **Session-Based & Interactive**

+ Uses **Streamlit session_state** to manage:
    - Loaded dataset
    - Selected features
    - Trained models
    - Prediction results
+ Supports smooth **multi-page interaction** between Home, Train, and Predict pages.

6. **Technical Stack**

+ Python 3.12
+ Streamlit for UI
+ Pandas for data handling
+ Scikit-learn for linear regression
+ Custom utilities for timing (`Timer`) and plotting (`plotly_scatter`)

**USAGE FLOW**
---

1. Load the dataset on the **Home** page.
2. Inspect the dataset and visualise feature-price relationships.
3. Train a **single-variable model** or **multi-variable model**.
4. Switch to the **Predict** page, adjust feature values with sliders, and get real-time house price predictions.

**QUICK START**
---

1. Clone the repository to your local machine.
2. Install the required dependencies with the command `pip install -r requirements.txt`.
3. Run the application with the command `streamlit run main.py`.
4. You can also try the application by visiting the following
   link:  
   [![Static Badge](https://img.shields.io/badge/Open%20in%20Streamlit-Daochashao-red?style=for-the-badge&logo=streamlit&labelColor=white)](https://ca-p-pre.streamlit.app/)

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
