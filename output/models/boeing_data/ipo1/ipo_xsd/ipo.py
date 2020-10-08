from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.example.com/IPO"


@dataclass
class AddressType:
    """
    :ivar name:
    :ivar street:
    :ivar city:
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


@dataclass
class ItemsType:
    """
    :ivar content:
    :ivar item:
    """
    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    item: List["ItemsType.Item"] = field(
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
        customer_comment: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="customerComment",
                type="Element",
                namespace="http://www.example.com/IPO",
                min_occurs=0,
                max_occurs=2
            )
        )
        ship_comment: List[str] = field(
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
        weight_kg: Optional[Decimal] = field(
            default=None,
            metadata=dict(
                name="weightKg",
                type="Attribute"
            )
        )
        ship_by: Optional["ItemsType.Item.ShipBy"] = field(
            default=None,
            metadata=dict(
                name="shipBy",
                type="Attribute"
            )
        )

        class ShipBy(Enum):
            """
            :cvar AIR:
            :cvar LAND:
            :cvar ANY:
            """
            AIR = "air"
            LAND = "land"
            ANY = "any"


class Usstate(Enum):
    """
    :cvar AK:
    :cvar AL:
    :cvar AR:
    :cvar CA:
    :cvar PA:
    """
    AK = "AK"
    AL = "AL"
    AR = "AR"
    CA = "CA"
    PA = "PA"


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
            namespace="",
            required=True
        )
    )
    bill_to: Optional[AddressType] = field(
        default=None,
        metadata=dict(
            name="billTo",
            type="Element",
            namespace="",
            required=True
        )
    )
    single_address: Optional[AddressType] = field(
        default=None,
        metadata=dict(
            name="singleAddress",
            type="Element",
            namespace=""
        )
    )
    customer_comment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="customerComment",
            type="Element",
            namespace="http://www.example.com/IPO"
        )
    )
    ship_comment: Optional[str] = field(
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
            namespace="",
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
class Ukaddress(AddressType):
    """
    :ivar postcode:
    :ivar export_code:
    """
    class Meta:
        name = "UKAddress"

    postcode: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True,
            pattern=r"[A-Z]{2}\d\s\d[A-Z]{2}"
        )
    )
    export_code: int = field(
        init=False,
        default=1,
        metadata=dict(
            name="exportCode",
            type="Attribute"
        )
    )


@dataclass
class Usaddress(AddressType):
    """
    :ivar state:
    :ivar zip:
    """
    class Meta:
        name = "USAddress"

    state: Optional[Usstate] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    zip: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class PurchaseOrder(PurchaseOrderType):
    class Meta:
        name = "purchaseOrder"
        namespace = "http://www.example.com/IPO"
