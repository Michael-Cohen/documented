"""This is an important module. """


def flow_function(x: int, y: str) -> str:
    """Sphinx-style doc of flow_function

    Additional documentation.

    :param x: an integer
    :param y: a string
    :return: the returned string
    """
    z = f"y... {x}"
    return z


def flow_function_bis(x: int, y: str) -> str:
    """Numpy-style doc of flow_function

    Additional documentation.

    Parameters
    ----------
    x : int
        an integer
    y : str
        a string

    Returns
    -------
    str
        The returned string
    """
    z = f"y... {x}"
    return z


def flow_function_ter(x: int, y: str) -> str:
    """Google-style doc of flow_function.

    Additional documentation.

    Args:
        x (int): an integer.
        y (int): a string.

    Returns:
        str: The returned string.

    """
    z = f"y... {x}"
    return z
