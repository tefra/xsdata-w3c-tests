from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.example.com/IPO"


class ItemShipBy(StrEnum):
    AIR = "air"
    LAND = "land"
    ANY = "any"
