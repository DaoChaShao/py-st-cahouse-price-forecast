#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/24 19:01
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   home.py
# @Desc     :

from pandas import read_csv, DataFrame
from streamlit import (title, empty, sidebar, subheader, selectbox,
                       caption, button, session_state, rerun)

from utils.helper import Timer

title("California House Price Forecast")

empty_messages: empty = empty()
empty_chart: empty = empty()
empty_table: empty = empty()

if "data" not in session_state:
    session_state["data"] = None

with sidebar:
    subheader("Data Management")
    datasets: list[str] = ["ca_house_prices.csv", ]
    dataset = selectbox(
        "Select Dataset", datasets, index=0, disabled=True,
        help="Select the dataset to be used for training and prediction."
    )
    caption(f"The dataset you selected is **{dataset}**.")

    if session_state.data is not None:
        empty_table.data_editor(session_state.data, hide_index=True, disabled=True, use_container_width=True)

        option: str = "median_house_value"
        price: str = selectbox(
            "Select Price Column", [option],
            help="Select the price column for training.", index=0, disabled=True
        )
        cols: list[str] = [c for c in session_state.data.columns if c != option]
        col: str = selectbox(
            "Select Target Column", ["select a col"] + cols,
            help="Select the target column for training."
        )
        if col == "select a col":
            empty_messages.success(
                f"The dataset **{dataset}** has been loaded successfully! Please select a target column to view charts."
            )
        else:
            empty_messages.info(f"You have selected **{col}** as the target column.")

            if button("Load Chart", type="primary", use_container_width=True):
                with Timer("Load the Chart") as timer:
                    empty_chart.scatter_chart(
                        session_state.data[[col, price]],
                        x=col,
                        y=price,
                        height=530,
                        use_container_width=True
                    )
                empty_messages.success(timer)
    else:
        empty_messages.warning("Please load the dataset first.")

        if button("Load Dataset", type="primary", use_container_width=True):
            with Timer("Loading dataset") as timer:
                session_state["data"]: DataFrame = read_csv(dataset)
                session_state["data"].drop(["latitude", "longitude", "ocean_proximity"], axis=1, inplace=True)
                empty_table.data_editor(session_state.data, hide_index=True, disabled=True, use_container_width=True)
            empty_messages.info(timer)
            rerun()
