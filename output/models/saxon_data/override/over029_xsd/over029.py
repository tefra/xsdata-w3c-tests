from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://datypic.com/ord"


@dataclass
class ProductType:
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datypic.com/ord",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datypic.com/ord",
            "required": True,
        }
    )
    size: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datypic.com/ord",
        }
    )
    gift_wrap: Optional[str] = field(
        default=None,
        metadata={
            "name": "giftWrap",
            "type": "Element",
            "namespace": "http://datypic.com/spc",
        }
    )
    points: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://datypic.com/spc",
        }
    )


@dataclass
class OrderType:
    product: Optional[ProductType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datypic.com/ord",
            "required": True,
        }
    )


@dataclass
class Order(OrderType):
    class Meta:
        name = "order"
        namespace = "http://datypic.com/ord"
