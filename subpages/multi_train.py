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
                       selectbox, button, columns, metric, rerun)

from subpages.single_train import MSE, R2
from utils.helper import Timer, plotly_scatter

empty_messages: empty = empty()
left, right = columns(2, gap="large")
empty_chart: empty = empty()
empty_table: empty = empty()

if "data" not in session_state:
    session_state["data"] = None
# if "price" not in session_state:
#     session_state["price"] = ""
if "model_multi" not in session_state:
    session_state["model_multi"] = None
if "Y_multi" not in session_state:
    session_state["Y_multi"] = None
if "y_multi" not in session_state:
    session_state["y_multi"] = None
if "selected_multi" not in session_state:
    session_state["selected_multi"] = None
if "clicked_multi" not in session_state:
    session_state["clicked_multi"] = False

with sidebar:
    subheader("Data Training Settings")

    if session_state.data is None:
        empty_messages.error("Please upload data on the **Home** page.")
    else:
        option: str = "median_house_value"
        price: str = selectbox(
            "Select a variable for y", [option],
            help="Select the price column for training.", index=0, disabled=True
        )
        multi_options: list[str] = [col for col in session_state["data"].columns if col != price]
        multi: list[str] = multiselect(
            "Select variables for X",
            multi_options,
            default=[col for col in session_state["selected_multi"] if col in multi_options] if session_state["selected_multi"] else [],
            disabled=session_state["clicked_multi"],
            help="Select the target variables for training with multiple variables.",
        )
        session_state["selected_multi"] = multi
        if not multi:
            empty_messages.warning("Please select at least one variable for training.")
        else:
            X_multi: DataFrame = session_state["data"].drop([price], axis=1)
            empty_table.data_editor(X_multi[multi], hide_index=True, disabled=True, use_container_width=True)

            if session_state["model_multi"] is not None:
                mse_multi: float = mean_squared_error(session_state.Y_multi, session_state.y_multi)
                mse_multi_sqrt: float = sqrt(mse_multi)
                r2_multi: float = r2_score(session_state.Y_multi, session_state.y_multi)
                with left:
                    metric("Mean Squared Error", f"{mse_multi_sqrt:.2f}",
                           delta=f"{mse_multi_sqrt - MSE:.2f}")
                with right:
                    metric("R² Score", f"{r2_multi:.4f}", delta=f"{r2_multi - R2:.4f}")
                empty_chart.plotly_chart(
                    plotly_scatter(session_state.Y_multi, session_state.y_multi, ", ".join(multi)),
                    use_container_width=True
                )
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
                            session_state["Y_multi"] = session_state["data"][price].loc[X_multi.index]
                            # Train the model
                            session_state["model_multi"]: LinearRegression = LinearRegression()
                            session_state["model_multi"].fit(X_multi, session_state.Y_multi)
                            # Get the predictions
                            session_state["y_multi"] = session_state["model_multi"].predict(X_multi)

                            mse_multi: float = mean_squared_error(session_state.Y_multi, session_state.y_multi)
                            mse_multi_sqrt: float = sqrt(mse_multi)
                            r2_multi: float = r2_score(session_state.Y_multi, session_state.y_multi)
                            with left:
                                metric("Mean Squared Error", f"{mse_multi_sqrt:.2f}",
                                       delta=f"{mse_multi_sqrt - MSE:.2f}")
                            with right:
                                metric("R² Score", f"{r2_multi:.4f}", delta=f"{r2_multi - R2:.4f}")
                            empty_chart.plotly_chart(
                                plotly_scatter(session_state.Y_multi, session_state.y_multi, ", ".join(multi)),
                                use_container_width=True
                            )
                        empty_messages.success(f"Model trained successfully! {timer}")
                        session_state["clicked_multi"] = True
                        rerun()
