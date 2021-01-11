from enum import Enum

__NAMESPACE__ = "http://www.example.com/att"


class ItemDeliveryShipBy(Enum):
    AIR = "air"
    LAND = "land"
    ANY = "any"
