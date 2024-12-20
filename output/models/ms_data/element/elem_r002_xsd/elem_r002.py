from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "testNS"


@dataclass
class Usaddress:
    class Meta:
        name = "USAddress"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    street: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    country: str = field(
        default="US",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Comment:
    class Meta:
        name = "comment"
        namespace = "testNS"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class PurchaseOrderType:
    ship_to: Optional[Usaddress] = field(
        default=None,
        metadata={
            "name": "shipTo",
            "type": "Element",
            "namespace": "testNS",
            "required": True,
        },
    )
    bill_to: Optional[Usaddress] = field(
        default=None,
        metadata={
            "name": "billTo",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    comment: Optional[Comment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "testNS",
        },
    )


@dataclass
class PurchaseOrder(PurchaseOrderType):
    class Meta:
        name = "purchaseOrder"
        namespace = "testNS"
