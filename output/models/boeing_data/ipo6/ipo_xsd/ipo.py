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
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
            "required": True,
        }
    )
    street: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
            "required": True,
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
            "required": True,
        }
    )


@dataclass
class ItemsType:
    """
    :ivar content:
    :ivar item:
    """
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    item: List["ItemsType.Item"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
        }
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
            metadata={
                "name": "productName",
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
                "required": True,
            }
        )
        quantity: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
                "required": True,
                "max_exclusive": 100,
            }
        )
        usprice: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "USPrice",
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
                "required": True,
            }
        )
        customer_comment: List[str] = field(
            default_factory=list,
            metadata={
                "name": "customerComment",
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
                "max_occurs": 2,
            }
        )
        ship_comment: List[str] = field(
            default_factory=list,
            metadata={
                "name": "shipComment",
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
                "max_occurs": 2,
            }
        )
        comment: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
                "max_occurs": 2,
            }
        )
        ship_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "shipDate",
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
            }
        )
        part_num: Optional[str] = field(
            default=None,
            metadata={
                "name": "partNum",
                "type": "Attribute",
                "required": True,
                "pattern": r"\d{3}-[A-Z]{2}",
            }
        )
        weight_kg: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "weightKg",
                "type": "Attribute",
            }
        )
        ship_by: Optional["ItemsType.Item.ShipBy"] = field(
            default=None,
            metadata={
                "name": "shipBy",
                "type": "Attribute",
            }
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
        metadata={
            "required": True,
        }
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
        metadata={
            "required": True,
        }
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
        metadata={
            "required": True,
        }
    )


@dataclass
class PurchaseOrderType:
    """
    :ivar salutation:
    :ivar extern_first_element:
    :ivar ship_to:
    :ivar bill_to:
    :ivar single_address:
    :ivar customer_comment:
    :ivar ship_comment:
    :ivar comment:
    :ivar items:
    :ivar order_date:
    """
    salutation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/add",
            "required": True,
        }
    )
    extern_first_element: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternFirstElement",
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
            "required": True,
        }
    )
    ship_to: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "shipTo",
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
        }
    )
    bill_to: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "billTo",
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
        }
    )
    single_address: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "singleAddress",
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
        }
    )
    customer_comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerComment",
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
        }
    )
    ship_comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "shipComment",
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
        }
    )
    items: Optional[ItemsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
            "required": True,
        }
    )
    order_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "orderDate",
            "type": "Attribute",
        }
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
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
            "required": True,
            "pattern": r"[A-Z]{2}\d\s\d[A-Z]{2}",
        }
    )
    export_code: int = field(
        init=False,
        default=1,
        metadata={
            "name": "exportCode",
            "type": "Attribute",
        }
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
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
            "required": True,
        }
    )
    zip: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
            "required": True,
        }
    )


@dataclass
class Address(AddressType):
    class Meta:
        name = "address"
        namespace = "http://www.example.com/IPO"


@dataclass
class PurchaseOrder(PurchaseOrderType):
    class Meta:
        name = "purchaseOrder"
        namespace = "http://www.example.com/IPO"
