#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/24 19:23
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   single_predict.py
# @Desc     :   

from numpy import abs
from streamlit import (empty, sidebar, subheader, session_state, slider,
                       caption, button)

from utils.helper import Timer

empty_messages: empty = empty()
empty_metrics: empty = empty()

if "data" not in session_state:
    session_state["data"] = None
if "model" not in session_state:
    session_state["model"] = None
if "selected" not in session_state:
    session_state["selected"] = None

with sidebar:
    subheader("Data Prediction Settings")

    if session_state.data is None and session_state.model is None and session_state.selected is None:
        empty_messages.error("Please train the model on the **House Price Prediction Train** page first.")
    else:
        empty_messages.info("Model and Data loaded successfully. You can make predictions now.")
        # print(session_state.data)
        X = session_state.data[[session_state.selected]] * 10_000

        col_value: float = slider(
            "Select Feature Value",
            min_value=float(X[session_state.selected].min()),
            max_value=float(X[session_state.selected].max()),
            value=float(X[session_state.selected].mean()),
            step=(float(X[session_state.selected].max()) - float(X[session_state.selected].min())) / len(X),
            help="Select the feature value for prediction."
        )
        caption(f"The value of the column is {col_value:.2f}")

        if button("Predict", type="primary", use_container_width=True):
            with Timer("Predict the House Price") as timer:
                # Find the original value Y
                index = abs(X.values - col_value).argmin()
                Y = session_state.Y.iloc[index]

                # Predict the value
                prediction = session_state.model.predict([[col_value]])
                empty_metrics.metric(
                    "Predicted House Price", f"$ {prediction[0]:.2f}", f"{prediction[0] - Y:.2f}"
                )
            empty_messages.success(timer)
