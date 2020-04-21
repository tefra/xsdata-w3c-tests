from decimal import Decimal
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.example.com/IPO"


@dataclass
class AddressType:
    """
    :ivar name:
    :ivar street:
    :ivar city:
    :ivar country:
    """
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
    city: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    country: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.example.com/IPO",
            required=True
        )
    )


@dataclass
class CustomerComment:
    """
    :ivar value:
    """
    class Meta:
        name = "customerComment"
        namespace = "http://www.example.com/IPO"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class ShipComment:
    """
    :ivar value:
    """
    class Meta:
        name = "shipComment"
        namespace = "http://www.example.com/IPO"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class ItemsType:
    """
    :ivar item:
    """
    item: List["ItemsType.Item"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.example.com/IPO",
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
        :ivar customer_comment:
        :ivar ship_comment:
        :ivar comment:
        :ivar ship_date:
        :ivar part_num:
        :ivar weight_kg:
        :ivar ship_by:
        """
        product_name: Optional[str] = field(
            default=None,
            metadata=dict(
                name="productName",
                type="Element",
                namespace="http://www.example.com/IPO",
                required=True
            )
        )
        quantity: Optional[int] = field(
            default=None,
            metadata=dict(
                type="Element",
                namespace="http://www.example.com/IPO",
                required=True,
                max_exclusive=100.0
            )
        )
        usprice: Optional[Decimal] = field(
            default=None,
            metadata=dict(
                name="USPrice",
                type="Element",
                namespace="http://www.example.com/IPO",
                required=True
            )
        )
        customer_comment: List[CustomerComment] = field(
            default_factory=list,
            metadata=dict(
                name="customerComment",
                type="Element",
                namespace="http://www.example.com/IPO",
                min_occurs=0,
                max_occurs=2
            )
        )
        ship_comment: List[ShipComment] = field(
            default_factory=list,
            metadata=dict(
                name="shipComment",
                type="Element",
                namespace="http://www.example.com/IPO",
                min_occurs=0,
                max_occurs=2
            )
        )
        comment: List[str] = field(
            default_factory=list,
            metadata=dict(
                type="Element",
                namespace="http://www.example.com/IPO",
                min_occurs=0,
                max_occurs=2
            )
        )
        ship_date: Optional[str] = field(
            default=None,
            metadata=dict(
                name="shipDate",
                type="Element",
                namespace="http://www.example.com/IPO"
            )
        )
        part_num: Optional[str] = field(
            default=None,
            metadata=dict(
                name="partNum",
                type="Attribute",
                namespace="http://www.example.com/att",
                required=True,
                pattern=r"\d{3}-[A-Z]{2}"
            )
        )
        weight_kg: Optional[Decimal] = field(
            default=None,
            metadata=dict(
                name="weightKg",
                type="Attribute",
                namespace="http://www.example.com/att"
            )
        )
        ship_by: Optional["ItemsType.Item.ShipBy"] = field(
            default=None,
            metadata=dict(
                name="shipBy",
                type="Attribute",
                namespace="http://www.example.com/att"
            )
        )

        class ShipBy(Enum):
            """
            :cvar AIR:
            :cvar ANY:
            :cvar LAND:
            """
            AIR = "air"
            ANY = "any"
            LAND = "land"


@dataclass
class PurchaseOrderType:
    """
    :ivar ship_to:
    :ivar bill_to:
    :ivar single_address:
    :ivar customer_comment:
    :ivar ship_comment:
    :ivar comment:
    :ivar items:
    :ivar order_date:
    """
    ship_to: Optional[AddressType] = field(
        default=None,
        metadata=dict(
            name="shipTo",
            type="Element",
            namespace="http://www.example.com/IPO",
            required=True
        )
    )
    bill_to: Optional[AddressType] = field(
        default=None,
        metadata=dict(
            name="billTo",
            type="Element",
            namespace="http://www.example.com/IPO",
            required=True
        )
    )
    single_address: Optional[AddressType] = field(
        default=None,
        metadata=dict(
            name="singleAddress",
            type="Element",
            namespace="http://www.example.com/IPO"
        )
    )
    customer_comment: Optional[CustomerComment] = field(
        default=None,
        metadata=dict(
            name="customerComment",
            type="Element",
            namespace="http://www.example.com/IPO"
        )
    )
    ship_comment: Optional[ShipComment] = field(
        default=None,
        metadata=dict(
            name="shipComment",
            type="Element",
            namespace="http://www.example.com/IPO"
        )
    )
    comment: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.example.com/IPO"
        )
    )
    items: Optional[ItemsType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.example.com/IPO",
            required=True
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
