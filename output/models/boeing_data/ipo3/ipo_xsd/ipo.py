from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Type
from xsdata.models.datatype import XmlDate
from output.models.boeing_data.ipo3.ipo_xsd.address import AddressType
from output.models.boeing_data.ipo3.ipo_xsd.itematt import ItemShipBy

__NAMESPACE__ = "http://www.example.com/IPO"


@dataclass
class CustomerComment:
    class Meta:
        name = "customerComment"
        namespace = "http://www.example.com/IPO"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class ShipComment:
    class Meta:
        name = "shipComment"
        namespace = "http://www.example.com/IPO"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
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
        },
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
            },
        )
        quantity: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
                "required": True,
                "max_exclusive": 100,
            },
        )
        usprice: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "USPrice",
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
                "required": True,
            },
        )
        customer_comment_or_ship_comment_or_comment: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "customerComment",
                        "type": str,
                        "namespace": "http://www.example.com/IPO",
                    },
                    {
                        "name": "shipComment",
                        "type": str,
                        "namespace": "http://www.example.com/IPO",
                    },
                    {
                        "name": "comment",
                        "type": str,
                        "namespace": "http://www.example.com/IPO",
                    },
                ),
                "max_occurs": 2,
            },
        )
        ship_date: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "shipDate",
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
            },
        )
        part_num: Optional[str] = field(
            default=None,
            metadata={
                "name": "partNum",
                "type": "Attribute",
                "required": True,
                "pattern": r"\d{3}-[A-Z]{2}",
            },
        )
        weight_kg: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "weightKg",
                "type": "Attribute",
            },
        )
        ship_by: Optional[ItemShipBy] = field(
            default=None,
            metadata={
                "name": "shipBy",
                "type": "Attribute",
            },
        )


@dataclass
class PurchaseOrderType:
    ship_to_or_bill_to_or_single_address: List[AddressType] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "shipTo",
                    "type": AddressType,
                    "namespace": "http://www.example.com/IPO",
                },
                {
                    "name": "billTo",
                    "type": AddressType,
                    "namespace": "http://www.example.com/IPO",
                },
                {
                    "name": "singleAddress",
                    "type": AddressType,
                    "namespace": "http://www.example.com/IPO",
                },
            ),
            "max_occurs": 2,
        },
    )
    customer_comment_or_ship_comment_or_comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "customerComment",
                    "type": str,
                    "namespace": "http://www.example.com/IPO",
                },
                {
                    "name": "shipComment",
                    "type": str,
                    "namespace": "http://www.example.com/IPO",
                },
                {
                    "name": "comment",
                    "type": str,
                    "namespace": "http://www.example.com/IPO",
                },
            ),
        },
    )
    items: Optional[ItemsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
            "required": True,
        },
    )
    order_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "orderDate",
            "type": "Attribute",
            "namespace": "http://www.example.com/IPO",
        },
    )


@dataclass
class PurchaseOrder(PurchaseOrderType):
    class Meta:
        name = "purchaseOrder"
        namespace = "http://www.example.com/IPO"
