import click
import numpy as np
import pandas as pd
from numpy import pi


@click.group()
def cmd_group():
    pass


@cmd_group.command()
@click.option("-n", "--number", default=1, help="Number of steps between 0 and pi")
def sin(number):
    """calculates sin between 0 and pi in number of given steps"""
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)


@cmd_group.command()
@click.option("-n", "--number", default=1, help="Number of steps between 0 and pi")
def tan(number):
    """calculates tan between 0 and pi in number of given steps"""
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


@cmd_group.command()
@click.argument("number", type=float)
def approx(number):
    """determines small-angle approximation with a certain accuracy"""
    i = 0
    while np.abs(i - np.sin(i)) <= number:
        i = i + 0.001
    print(
        f"For an accuracy of {number},the small-angle approximation holds up to x = {np.round(i,3)}"
    )


if __name__ == "__main__":
    cmd_group()
