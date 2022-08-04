import numbers


def check_is_integer(data: int) -> bool:
    """
    Check the given data is integer or not
    Args:
        num (Int) : Given data
    Return:
        Bool: True if num is integer, vice versa
    """
    if isinstance(data, int):
        return True
    else:
        False


def check_is_general_numeric(data) -> bool:
    """
    Check the given data is general numeric or not
    Args:
        num (Numeric) : Given data
    Return:
        Bool: True if num is general numeric , vice versa
    """
    if isinstance(data, numbers.Number):
        return True
    else:
        False


def check_is_list(data: list) -> bool:
    """
    Check the given data is list or not
    Args:
        data (List) : Given data
    Return:
        Bool: True if num is list , vice versa
    """
    if isinstance(data, list):
        return True
    else:
        return False


def check_float_in_range(data: float, min: float, max: float) -> bool:
    """
    Check the given data is in range [min, max] or not
    Args:
        data (Float) : Given data
        min (Float): Min of range
        max (Float): Max of range
    Return:
        Bool: True if num is list , vice versa
    """
    if min <= data <= max:
        return True
    else:
        return False


def _sorted(data: list) -> list:
    """
    Sort a list
    Args:
        data (List)
    Return:
        List: List sorted
    """
    return sorted(data)


def _len(data: list) -> int:
    """
    Calculate len of a list
    Args:
        data (List)
    Return:
        int: Len of given list
    """
    return len(data)
