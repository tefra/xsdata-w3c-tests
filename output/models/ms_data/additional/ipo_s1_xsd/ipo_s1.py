from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from output.models.ms_data.additional.ipo_s1_xsd.ipo_s1_address import Address

__NAMESPACE__ = "http://www.example.com/IPO"


@dataclass
class Items:
    item: List["Items.Item"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class Item:
        product_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "productName",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        quantity: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_exclusive": 100,
            }
        )
        usprice: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "USPrice",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        comment: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
            }
        )
        ship_date: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "shipDate",
                "type": "Element",
                "namespace": "",
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


@dataclass
class Comment:
    class Meta:
        name = "comment"
        namespace = "http://www.example.com/IPO"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class PurchaseOrderType:
    ship_to: Optional[Address] = field(
        default=None,
        metadata={
            "name": "shipTo",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    bill_to: Optional[Address] = field(
        default=None,
        metadata={
            "name": "billTo",
            "type": "Element",
            "namespace": "",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
        }
    )
    items: Optional[Items] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
