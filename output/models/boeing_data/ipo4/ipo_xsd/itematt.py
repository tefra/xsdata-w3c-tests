from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.example.com/att"


class ItemShipBy(StrEnum):
    AIR = "air"
    LAND = "land"
    ANY = "any"
