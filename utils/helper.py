#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/24 19:00
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   helper.py
# @Desc     :

from joblib import dump, load
from pandas import DataFrame
from plotly.express import scatter
from time import perf_counter


class Timer(object):
    """ timing code blocks using a context manager """

    def __init__(self, description: str = None, precision: int = 5):
        """ Initialise the Timer class
        :param description: the description of a timer
        :param precision: the number of decimal places to round the elapsed time
        """
        self._description: str = description
        self._precision: int = precision
        self._start: float = 0.0
        self._end: float = 0.0
        self._elapsed: float = 0.0

    def __enter__(self):
        """ Start the timer """
        self._start = perf_counter()
        print()
        print("-" * 50)
        print(f"{self._description} has been started.")
        return self

    def __exit__(self, *args):
        """ Stop the timer and calculate the elapsed time """
        self._end = perf_counter()
        self._elapsed = self._end - self._start

    def __repr__(self):
        """ Return a string representation of the timer """
        if self._elapsed != 0.0:
            print("-" * 50)
            return f"{self._description} took {self._elapsed:.{self._precision}f} seconds."
        return f"{self._description} has NOT been started."


def plotly_scatter(Y, y, target_col: str):
    """ Plotly Scatter Plot with OLS Trendline
    :param Y: Actual values
    :param y: Predicted values
    :param target_col: The name of the target column
    :return: A Plotly Scatter Plot with OLS Trendline
    """
    df: DataFrame = DataFrame({
        f"{target_col}": Y,
        f"{target_col} Predicted": y
    })
    return scatter(
        df,
        x=f"{target_col}",
        y=f"{target_col} Predicted",
        trendline="ols",
        trendline_color_override="red",
        opacity=0.4,
        labels={f"{target_col}": f"Actual Y", f"{target_col} Predicted": "Predicted y"},
        title=f"{target_col} Actual vs Predicted"
    )


def model_saver(model, filename: str) -> None:
    """ Save the model to a file
    :param model: The model to be saved
    :param filename: The name of the file to save the model to
    """
    dump(model, filename)
    print(f"The model {filename} has been saved successfully.")


def model_loader(filename: str):
    """ Load the model from a file
    :param filename: The name of the file to load the model from
    :return: The loaded model
    """
    model = load(filename)
    print(f"The model {filename} has been loaded successfully.")
    return model
