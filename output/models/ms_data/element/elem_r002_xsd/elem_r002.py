from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "testNS"


@dataclass(kw_only=True)
class Usaddress:
    class Meta:
        name = "USAddress"

    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    street: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    country: str = field(
        default="US",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Comment:
    class Meta:
        name = "comment"
        namespace = "testNS"

    value: str = field(default="")


@dataclass(kw_only=True)
class PurchaseOrderType:
    ship_to: Usaddress = field(
        metadata={
            "name": "shipTo",
            "type": "Element",
            "namespace": "testNS",
        }
    )
    bill_to: Usaddress = field(
        metadata={
            "name": "billTo",
            "type": "Element",
            "namespace": "",
        }
    )
    comment: None | Comment = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "testNS",
        },
    )


@dataclass(kw_only=True)
class PurchaseOrder(PurchaseOrderType):
    class Meta:
        name = "purchaseOrder"
        namespace = "testNS"
