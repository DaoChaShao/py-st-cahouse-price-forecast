#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/24 19:01
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   about.py
# @Desc     :

from streamlit import title, expander, caption

title("Application Information")

with expander("About this application", expanded=True):
    caption("**California House Price Forecast** is an interactive Streamlit app for exploring, visualizing, training, and predicting California house prices using linear regression models.")
    caption("+ Load and preprocess the California housing dataset.")
    caption("+ Interactive dataset viewing with read-only tables.")
    caption("+ Visualize feature vs. price relationships with scatter charts.")
    caption("+ Train single-variable linear regression models.")
    caption("+ Train multi-variable linear regression models.")
    caption("+ Display evaluation metrics: MSE, RMSE, R² Score.")
    caption("+ Interactive sliders for feature selection and prediction.")
    caption("+ Compare predicted vs actual house prices visually.")
    caption("+ Session-based state management for smooth multi-page interaction.")
    caption("+ Built with Python 3.12, Streamlit, Pandas, Scikit-learn, and Plotly.")

