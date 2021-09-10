"""
Advanced Calculus 2DBN10 Assignment 1, Group 1-8

Author: Lulof Pirée (1363638)

Code for Problem 2e.
"""
import numpy as np
import matplotlib.pyplot as plt
from typing import Iterable

def argmax_omega(p: float) -> float:
    """
    Return the value of ω that maximizes the amplitude of
    y_p(t) for the given value of 'p'.
    """
    return np.sqrt(1 - 0.5 * (p**2))

def amplitude(ω: float, p: float) -> float:
    """
    Return the maximum amplitude reached by y_p(t)
    for the given parameters.
    """
    return 1 / np.sqrt(ω**4 + (p**2 - 2)*(ω**2) + 1)

def plot_amplitude(p_values: Iterable[float]):
    for p in p_values:
        ω_values = np.arange(0.01, 10, step = 0.1)
        y_values = amplitude(ω_values, p)
        label=f"p={p}"
        plt.plot(ω_values, y_values, label=label)
    plt.xlabel("ω")
    plt.ylabel("$y_p$")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot_amplitude([0.2, 0.05])

