#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/24 19:24
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   multi_train.py
# @Desc     :   

from numpy import sqrt
from pandas import DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from streamlit import (empty, sidebar, subheader, session_state, multiselect,
                       selectbox, button, columns, metric)

from subpages.single_train import MSE, R2
from utils.helper import Timer, plotly_scatter

empty_messages: empty = empty()
left, right = columns(2, gap="large")
empty_chart: empty = empty()
empty_table: empty = empty()

# if "price" not in session_state:
#     session_state["price"] = ""
if "data" not in session_state:
    session_state["data"] = None
if "model_multi" not in session_state:
    session_state["model_multi"] = None

with sidebar:
    subheader("Data Training Settings")

    if session_state.data is None:
        empty_messages.error("Please upload data on the **Home** page.")
    else:
        price: str = selectbox(
            "Select a variable for y", [session_state.price],
            help="Select the price column for training.", index=0, disabled=True
        )
        multi_options: list[str] = [c for c in session_state["data"].columns if c != session_state["price"]]
        multi: list[str] = multiselect(
            "Select variables for X",
            multi_options,
            default=multi_options,
            # disabled=True,
            help="Select the target variables for training with multiple variables.",
        )
        X_multi: DataFrame = session_state["data"].drop([session_state.price], axis=1)
        empty_table.data_editor(X_multi[multi], hide_index=True, disabled=True, use_container_width=True)

        if session_state["model_multi"] is not None:
            empty_messages.success("The model has been trained with multiple variables.")
        else:
            if len(multi) == 0:
                empty_messages.warning("Please select at least one variable for training.")
            else:

                empty_messages.info(f"Training model with {len(multi)} variables.")
                if button("Train Model", type="primary", use_container_width=True):
                    with Timer("Training Model with variables") as timer:
                        # Set the data
                        X_multi = X_multi.dropna()
                        Y_multi = session_state["data"][session_state.price].loc[X_multi.index]
                        # Train the model
                        model_multi: LinearRegression = LinearRegression()
                        model_multi.fit(X_multi, Y_multi)
                        # Get the predictions
                        y_multi = model_multi.predict(X_multi)

                        mse_multi: float = mean_squared_error(Y_multi, y_multi)
                        mse_multi_sqrt: float = sqrt(mse_multi)
                        r2_multi: float = r2_score(Y_multi, y_multi)
                        with left:
                            metric("Mean Squared Error", f"{mse_multi_sqrt:.2f}", delta=f"{mse_multi_sqrt - MSE:.2f}")
                        with right:
                            metric("R² Score", f"{r2_multi:.4f}", delta=f"{r2_multi - R2:.4f}")
                        empty_chart.plotly_chart(
                            plotly_scatter(Y_multi, y_multi, ", ".join(multi)),
                            use_container_width=True
                        )
                    empty_messages.success("Model trained successfully!")
