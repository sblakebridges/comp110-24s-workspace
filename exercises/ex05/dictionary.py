"""Dictionary EX05!"""

__author__ = "730643380"


def invert(dic: dict[str, str]) -> dict[str, str]:
    """Invert!!!"""
    inverted_dict = {}
    for key in dic:
        if dic[key] in inverted_dict:
            raise KeyError("Wrong!")
        inverted_dict[dic[key]] = key
    return inverted_dict


def favorite_color(colors_dic: dict[str, str]) -> str:
    """Favorite!"""
    colors: dict[str, int] = {}
    for key in colors_dic:
        value = colors_dic[key]
        if colors_dic[key] in colors:
            colors[value] += 1
        else:
            colors[value] = 1
    fav_color = ""
    max_value = 0
    for c in colors:
        if max_value < colors[c]:
            max_value = colors[c]
            fav_color = c
    return fav_color


def count(cnt: list[str]) -> dict[str, int]:
    """Count!"""
    counting: dict[str, int] = {}
    for i in cnt:
        if i in counting:
            counting[i] += 1
        else:
            counting[i] = 1
    return counting


def alphabetizer(abc: list[str]) -> dict[str, list[str]]:
    """Alphabetizer!!!"""
    dicout: dict[str, list[str]] = {}
    for i in abc:
        if i[0].lower() in dicout:
            dicout[i[0].lower()].append(i)
        else:
            dicout[i[0].lower()] = [i]
    return dicout


def update_attendance(dicin: dict[str, list[str]], up: str, attend: str) -> None:
    """Update!!!"""
    if up in dicin:
        if not (attend in dicin[up]):
            dicin[up].append(attend)
    else:
        dicin[up] = [attend]