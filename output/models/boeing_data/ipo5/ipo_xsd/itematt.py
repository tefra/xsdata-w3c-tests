from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.example.com/IPO"


class ItemShipBy(Enum):
    AIR = "air"
    LAND = "land"
    ANY = "any"
