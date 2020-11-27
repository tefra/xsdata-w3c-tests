from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union


@dataclass
class Item:
    class Meta:
        name = "ITEM"

    quantity: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    price: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )


@dataclass
class LongItemDefn(Item):
    class Meta:
        name = "LONG_ITEM_DEFN"

    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ShortItemDefn(Item):
    class Meta:
        name = "SHORT_ITEM_DEFN"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Poitems:
    class Meta:
        name = "POITEMS"

    item: List[Union[Item, LongItemDefn, ShortItemDefn]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
