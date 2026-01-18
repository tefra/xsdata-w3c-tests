from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.example.com/att"


class ItemShipBy(Enum):
    AIR = "air"
    LAND = "land"
    ANY = "any"
