from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Type
from xsdata.models.datatype import XmlDate
from output.models.boeing_data.ipo5.ipo_xsd.address import AddressType
from output.models.boeing_data.ipo5.ipo_xsd.itematt import ItemDeliveryShipBy

__NAMESPACE__ = "http://www.example.com/IPO"


class Usstate(Enum):
    AK = "AK"
    AL = "AL"
    AR = "AR"
    CA = "CA"
    PA = "PA"


@dataclass
class Comment:
    class Meta:
        name = "comment"
        namespace = "http://www.example.com/IPO"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class CustomerComment:
    class Meta:
        name = "customerComment"
        namespace = "http://www.example.com/IPO"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class ShipComment:
    class Meta:
        name = "shipComment"
        namespace = "http://www.example.com/IPO"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class ItemsType:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "item",
                    "type": Type["ItemsType.Item"],
                    "namespace": "http://www.example.com/IPO",
                },
            ),
        }
    )

    @dataclass
    class Item:
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
        ship_date: Optional[XmlDate] = field(
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
        ship_by: Optional[ItemDeliveryShipBy] = field(
            default=None,
            metadata={
                "name": "shipBy",
                "type": "Attribute",
            }
        )


@dataclass
class Ukaddress(AddressType):
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
class PurchaseOrderType:
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
    order_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "orderDate",
            "type": "Attribute",
        }
    )


@dataclass
class PurchaseOrder(PurchaseOrderType):
    class Meta:
        name = "purchaseOrder"
        namespace = "http://www.example.com/IPO"
