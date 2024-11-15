import click
import numpy as np
import pandas as pd
from numpy import pi


@click.command()
# @click.argument("number")
@click.option("-n", "--numbersteps", default=1)
def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)


def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    sin()
    tan()
