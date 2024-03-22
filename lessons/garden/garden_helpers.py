"""Some functions for my garden plan!"""

__author__ = "730643380"


def add_by_kind(dicin: dict[str, list[str]], plant: str, type: str) -> None:
    """Adds plant type!"""
    if plant in dicin:
        dicin[plant].append(type)
    else:
        dicin[plant] = [type]


def add_by_date(dicin: dict[str, list[str]], month: str, plant: str) -> None:
    """Adds plant by date!"""
    if month in dicin:
        dicin[month].append(plant)
    else:
        dicin[month] = [plant]


def lookup_by_kind_and_date(dicin: dict[str, list[str]], dicout: dict[str, list[str]], kind: str, plant_date: str) -> str:
    """Uses two dictionaries to make a list of what plants of a certain kind to plant at a certain date."""
    right_plants: list[str] = []
    if kind in dicin and plant_date in dicout:
        for plant1 in dicin[kind]:
            for plant2 in dicout[plant_date]:
                if plant1 == plant2:
                    right_plants.append(plant1)
    
    if len(right_plants) == 0:
        return f"No {kind}s to plant in {plant_date}."
    else:
        return f"{kind}s to plant in {plant_date}: {right_plants}"