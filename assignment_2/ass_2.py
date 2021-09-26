"""
Advanced Calculus 2DBN10 Assignment 2, Group 1-8

Author: Lulof Pirée (1363638)

Code for Problem 1a.
"""
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, Iterable

def I(a:float) -> Callable[float, float]:
    return lambda t : (t <= a) * (1/a)

def make_plot(a_values:Iterable[float]):
    t_values = np.arange(0, 10, 0.01)
    for a in a_values:
        y_values = I(a)(t_values)
        plt.plot(t_values, y_values, label=f"a = {a}")
    plt.show()



if __name__ == "__main__":
    make_plot([1, 0.5, 0.2])

