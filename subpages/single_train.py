#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/24 19:02
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   single_train.py
# @Desc     :

from numpy import sqrt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from streamlit import (empty, sidebar, subheader, session_state, selectbox,
                       button, columns, metric, rerun)

from utils.helper import Timer, plotly_scatter

MSE: float = 0.0
R2: float = 1.0

empty_messages: empty = empty()
left, right = columns(2, gap="large")
empty_chart: empty = empty()
empty_formula: empty = empty()

if "data" not in session_state:
    session_state["data"] = None
if "model" not in session_state:
    session_state["model"] = None
if "X" not in session_state:
    session_state["X"] = None
if "Y" not in session_state:
    session_state["Y"] = None
if "y" not in session_state:
    session_state["y"] = None
if "clicked" not in session_state:
    session_state["clicked"] = False

with sidebar:
    subheader("Data Training Settings")

    if session_state.data is None:
        empty_messages.error("Please upload data on the **Home** page.")
    else:

        option: str = "median_house_value"
        price: str = selectbox(
            "Select Price Column", [option],
            help="Select the price column for training.", index=0, disabled=True
        )
        cols: list[str] = [c for c in session_state.data.columns if c != option]
        col: str = selectbox(
            "Select Target Column", cols, disabled=session_state.clicked,
            help="Select the target column for training."
        )

        if session_state.model is not None and session_state.Y is not None and session_state.y is not None:
            empty_messages.success(
                "Model already trained! You can retrain the model by selecting a different target column."
            )

            empty_formula.write(
                f"**$\\hat{{y}} = {session_state["model"].coef_[0]:.4f}x + {session_state["model"].intercept_:.4f}$**"
            )

            # Evaluate the model
            mse = mean_squared_error(session_state.Y, session_state.y)
            mse_sqrt = sqrt(mse)
            r2 = r2_score(session_state.Y, session_state.y)
            with left:
                metric("Mean Squared Error (MSE)", f"$ {mse_sqrt:.2f}", f"{mse_sqrt - MSE:.2f}")
            with right:
                metric("R² Score", f"{r2:.4f}", f"{r2 - R2:.4f}")
            empty_chart.plotly_chart(
                plotly_scatter(session_state.Y, session_state.y, col), use_container_width=True
            )
        else:
            empty_messages.info("Data uploaded successfully! Please select a target column to proceed with training.")

            if button("Train Model", type="primary", use_container_width=True):
                with Timer("Training Model") as timer:
                    # Prepare the data
                    session_state["X"] = session_state.data[[col]]
                    session_state["Y"] = session_state.data[price]

                    # Train the model
                    session_state["model"] = LinearRegression()
                    session_state["model"].fit(session_state.X, session_state.Y)
                    print("Coefficients:", session_state["model"].coef_)
                    print("Intercept:", session_state["model"].intercept_)
                    empty_formula.write(
                        f"**$\\hat{{y}} = {session_state["model"].coef_[0]:.4f}x + {session_state["model"].intercept_:.4f}$**"
                    )

                    # Make predictions
                    session_state["y"] = session_state["model"].predict(session_state.X)

                    # Evaluate the model
                    mse = mean_squared_error(session_state.Y, session_state.y)
                    mse_sqrt = sqrt(mse)
                    r2 = r2_score(session_state.Y, session_state.y)
                    with left:
                        metric("Mean Squared Error (MSE)", f"$ {mse_sqrt:.2f}", f"{mse_sqrt - MSE:.2f}")
                    with right:
                        metric("R² Score", f"{r2:.4f}", f"{r2 - R2:.4f}")
                    empty_chart.plotly_chart(
                        plotly_scatter(session_state.Y, session_state.y, col), use_container_width=True
                    )
                empty_messages.success(timer)
                session_state.clicked = True
                rerun()
