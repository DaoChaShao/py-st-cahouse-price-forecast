#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/24 19:24
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   multi_predict.py
# @Desc     :   

from streamlit import (empty, sidebar, subheader, session_state, write,
                       slider, columns, button, metric)

from utils.helper import Timer

empty_messages: empty = empty()
left, _ = columns(2, gap="large")

if "data" not in session_state:
    session_state["data"] = None
if "model_multi" not in session_state:
    session_state["model_multi"] = None
if "Y_multi" not in session_state:
    session_state["Y_multi"] = None

with sidebar:
    subheader("House Price Prediction Settings")

    if session_state.data is None:
        empty_messages.error("Please upload data on the **Home** page.")
    else:
        empty_messages.warning(
            "Please go to the **House Price Train with Multiple Variables** page to train the model first."
        )

        if session_state.model_multi is None:
            empty_messages.info("The model has not been trained yet.")
        else:
            empty_messages.success("The model has been trained with multiple variables.")

            # write(session_state["selected_multi"])
            for i, col in enumerate(session_state["selected_multi"]):
                value_min = float(session_state["data"][col].min())
                value_max = float(session_state["data"][col].max())
                value_mean = float(session_state["data"][col].mean())
                step = (value_max - value_min) / len(session_state["data"][col])
                slider(
                    f"Select {col}",
                    min_value=value_min,
                    max_value=value_max,
                    value=value_mean,
                    step=step,
                    help=f"Select the value of {col} for prediction."
                )

            if button("Predict House Price", type="primary", use_container_width=True):
                with Timer("House Price Prediction with Multiple Variables") as timer:
                    X_multi = session_state["data"][session_state["selected_multi"]].dropna()
                    y_multi = session_state["model_multi"].predict(X_multi)
                with left:
                    metric(
                        "Predicted House Price", f"$ {y_multi[0]:.2f}",
                        delta=f"{y_multi[0] - session_state["Y_multi"].mean():.2f}"
                    )
                empty_messages.info(timer)
