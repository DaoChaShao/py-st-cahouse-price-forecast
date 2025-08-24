#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/24 19:23
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   single_predict.py
# @Desc     :   

from streamlit import empty, sidebar, subheader, session_state

empty_messages: empty = empty()

if "X" not in session_state:
    session_state["X"] = None
if "model" not in session_state:
    session_state["model"] = None

with sidebar:
    subheader("Data Prediction Settings")

    empty_messages.info("This feature is under development. Please stay tuned!")
