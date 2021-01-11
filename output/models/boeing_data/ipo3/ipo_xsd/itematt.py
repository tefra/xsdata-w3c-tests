from enum import Enum

__NAMESPACE__ = "http://www.example.com/IPO"


class ItemDeliveryShipBy(Enum):
    AIR = "air"
    LAND = "land"
    ANY = "any"
