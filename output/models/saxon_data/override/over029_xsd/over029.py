from __future__ import annotations

from dataclasses import dataclass, field

from output.models.saxon_data.override.over029_xsd.over029a import GiftWrap

__NAMESPACE__ = "http://datypic.com/ord"


@dataclass(kw_only=True)
class ProductType:
    number: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://datypic.com/ord",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://datypic.com/ord",
            "required": True,
        }
    )
    size: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datypic.com/ord",
        },
    )
    gift_wrap: None | GiftWrap = field(
        default=None,
        metadata={
            "name": "giftWrap",
            "type": "Element",
            "namespace": "http://datypic.com/spc",
        },
    )
    points: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://datypic.com/spc",
        },
    )


@dataclass(kw_only=True)
class OrderType:
    product: ProductType = field(
        metadata={
            "type": "Element",
            "namespace": "http://datypic.com/ord",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Order(OrderType):
    class Meta:
        name = "order"
        namespace = "http://datypic.com/ord"
