"""EX07 - Dictionary Functions."""
__author__ = "730558551"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """New dictionary swapping keys and values."""
    dict_2: dict[str, str] = {}
    if dict_1 == {}:
        return {}
    for key in dict_1:
        dict_2[dict_1[key]] = key
    repeats: dict[str, int] = {}
    repeats = count(dict_1.values())
    if max(list(repeats.values())) > 1:
        raise KeyError("Repeating Keys Detected!!")
    return dict_2


def count(input_list: list[str]) -> dict[str, int]:
    """Given list of strings, creates dictionary of that list as keys and the number of times each item was repeated as the values."""
    result: dict[str, int] = {}
    for key in input_list:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Most common answer in a dict."""
    if colors == {}:
        return ""
    color_2 = count(list(colors.values()))
    keys = list(color_2.keys())
    values = list(color_2.values())
    index = values.index(max(values))
    return keys[index]