#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/24 19:01
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   home.py
# @Desc     :

from streamlit import title, expander, caption, empty

title("California House Price Forecast")

empty_message = empty()
empty_message.info("Please check the details at the different pages of core functions.")

with expander("INTRODUCTION", expanded=True):
    caption("")
