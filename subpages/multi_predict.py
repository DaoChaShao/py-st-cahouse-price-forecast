#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/24 19:24
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   multi_predict.py
# @Desc     :   

from streamlit import empty, sidebar, subheader, session_state

empty_messages: empty = empty()

if "data" not in session_state:
    session_state["data"] = None
if "model_multi" not in session_state:
    session_state["model_multi"] = None

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
            # Add your prediction code here
