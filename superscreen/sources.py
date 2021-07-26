from typing import Union

import numpy as np

from .parameter import Parameter


def constant(
    x: Union[int, float, np.ndarray],
    y: Union[int, float, np.ndarray],
    z: Union[int, float, np.ndarray],
    value: Union[int, float] = 0,
) -> Union[int, float, np.ndarray]:
    """Constant field.

    Args:
        x, y, z: Position coordinates.
        value: Value of the field.
    """
    return value * np.ones_like(x)


def ConstantField(value: float) -> Parameter:
    return Parameter(constant, value=value)
