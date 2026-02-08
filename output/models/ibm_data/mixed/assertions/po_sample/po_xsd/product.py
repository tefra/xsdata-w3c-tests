from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(kw_only=True)
class Item:
    class Meta:
        name = "ITEM"

    quantity: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    price: None | Decimal = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": Decimal("0"),
        },
    )


@dataclass(kw_only=True)
class LongItemDefn(Item):
    class Meta:
        name = "LONG_ITEM_DEFN"

    description: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class ShortItemDefn(Item):
    class Meta:
        name = "SHORT_ITEM_DEFN"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Poitems:
    class Meta:
        name = "POITEMS"

    item: list[Item | ShortItemDefn | LongItemDefn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
