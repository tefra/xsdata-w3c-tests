from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union


@dataclass
class Item:
    """
    :ivar quantity:
    :ivar price:
    """
    class Meta:
        name = "ITEM"

    quantity: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    price: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            min_inclusive=0
        )
    )


@dataclass
class LongItemDefn(Item):
    """
    :ivar description:
    """
    class Meta:
        name = "LONG_ITEM_DEFN"

    description: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class ShortItemDefn(Item):
    """
    :ivar id:
    """
    class Meta:
        name = "SHORT_ITEM_DEFN"

    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Poitems:
    """
    :ivar item:
    """
    class Meta:
        name = "POITEMS"

    item: List[Union[Item, LongItemDefn, ShortItemDefn]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
