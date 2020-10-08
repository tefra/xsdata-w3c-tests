from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from output.models.ms_data.additional.ipo_xsd.ipo_address import Address

__NAMESPACE__ = "http://www.example.com/IPO"


@dataclass
class Items:
    """
    :ivar item:
    """
    item: List["Items.Item"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class Item:
        """
        :ivar product_name:
        :ivar quantity:
        :ivar usprice:
        :ivar comment:
        :ivar ship_date:
        :ivar part_num:
        """
        product_name: Optional[str] = field(
            default=None,
            metadata=dict(
                name="productName",
                type="Element",
                namespace="",
                required=True
            )
        )
        quantity: Optional[int] = field(
            default=None,
            metadata=dict(
                type="Element",
                namespace="",
                required=True,
                max_exclusive=100
            )
        )
        usprice: Optional[Decimal] = field(
            default=None,
            metadata=dict(
                name="USPrice",
                type="Element",
                namespace="",
                required=True
            )
        )
        comment: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Element",
                namespace="http://www.example.com/IPO"
            )
        )
        ship_date: Optional[str] = field(
            default=None,
            metadata=dict(
                name="shipDate",
                type="Element",
                namespace=""
            )
        )
        part_num: Optional[str] = field(
            default=None,
            metadata=dict(
                name="partNum",
                type="Attribute",
                required=True,
                pattern=r"\d{3}-[A-Z]{2}"
            )
        )


@dataclass
class Comment:
    """
    :ivar value:
    """
    class Meta:
        name = "comment"
        namespace = "http://www.example.com/IPO"

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
    :ivar items:
    :ivar order_date:
    """
    ship_to: Optional[Address] = field(
        default=None,
        metadata=dict(
            name="shipTo",
            type="Element",
            namespace="",
            required=True
        )
    )
    bill_to: Optional[Address] = field(
        default=None,
        metadata=dict(
            name="billTo",
            type="Element",
            namespace=""
        )
    )
    comment: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.example.com/IPO"
        )
    )
    items: Optional[Items] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    order_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="orderDate",
            type="Attribute"
        )
    )


@dataclass
class PurchaseOrder(PurchaseOrderType):
    class Meta:
        name = "purchaseOrder"
        namespace = "http://www.example.com/IPO"
