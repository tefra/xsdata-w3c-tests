from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "testNS"


@dataclass
class Usaddress:
    """
    :ivar name:
    :ivar street:
    :ivar country:
    """
    class Meta:
        name = "USAddress"

    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    street: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    country: str = field(
        default="US",
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Comment:
    """
    :ivar value:
    """
    class Meta:
        name = "comment"
        namespace = "testNS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class PurchaseOrderType:
    """
    :ivar ship_to:
    :ivar bill_to:
    :ivar comment:
    """
    ship_to: Optional[Usaddress] = field(
        default=None,
        metadata=dict(
            name="shipTo",
            type="Element",
            namespace="testNS",
            required=True
        )
    )
    bill_to: Optional[Usaddress] = field(
        default=None,
        metadata=dict(
            name="billTo",
            type="Element",
            namespace="",
            required=True
        )
    )
    comment: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="testNS"
        )
    )


@dataclass
class PurchaseOrder(PurchaseOrderType):
    class Meta:
        name = "purchaseOrder"
        namespace = "testNS"
