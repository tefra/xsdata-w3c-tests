from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import ForwardRef

from xsdata.models.datatype import XmlDate

from output.models.boeing_data.ipo3.ipo_xsd.address import AddressType
from output.models.boeing_data.ipo3.ipo_xsd.itematt import ItemShipBy

__NAMESPACE__ = "http://www.example.com/IPO"


@dataclass(kw_only=True)
class Comment:
    class Meta:
        name = "comment"
        namespace = "http://www.example.com/IPO"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class ItemsType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "item",
                    "type": ForwardRef("ItemsType.Item"),
                    "namespace": "http://www.example.com/IPO",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Item:
        product_name: str = field(
            metadata={
                "name": "productName",
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
                "required": True,
            }
        )
        quantity: int = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
                "required": True,
                "max_exclusive": 100,
            }
        )
        usprice: Decimal = field(
            metadata={
                "name": "USPrice",
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
                "required": True,
            }
        )
        customer_comment_or_ship_comment: list[
            CustomerComment | ShipComment
        ] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "customerComment",
                        "type": CustomerComment,
                        "namespace": "http://www.example.com/IPO",
                        "max_occurs": 2,
                    },
                    {
                        "name": "shipComment",
                        "type": ShipComment,
                        "namespace": "http://www.example.com/IPO",
                        "max_occurs": 2,
                    },
                ),
                "max_occurs": 2,
            },
        )
        ship_date: None | XmlDate = field(
            default=None,
            metadata={
                "name": "shipDate",
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
            },
        )
        part_num: str = field(
            metadata={
                "name": "partNum",
                "type": "Attribute",
                "required": True,
                "pattern": r"\d{3}-[A-Z]{2}",
            }
        )
        weight_kg: None | Decimal = field(
            default=None,
            metadata={
                "name": "weightKg",
                "type": "Attribute",
            },
        )
        ship_by: None | ItemShipBy = field(
            default=None,
            metadata={
                "name": "shipBy",
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class PurchaseOrderType:
    ship_to_or_bill_to_or_single_address: list[
        PurchaseOrderType.ShipTo
        | PurchaseOrderType.BillTo
        | PurchaseOrderType.SingleAddress
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "shipTo",
                    "type": ForwardRef("PurchaseOrderType.ShipTo"),
                    "namespace": "http://www.example.com/IPO",
                },
                {
                    "name": "billTo",
                    "type": ForwardRef("PurchaseOrderType.BillTo"),
                    "namespace": "http://www.example.com/IPO",
                },
                {
                    "name": "singleAddress",
                    "type": ForwardRef("PurchaseOrderType.SingleAddress"),
                    "namespace": "http://www.example.com/IPO",
                },
            ),
            "max_occurs": 2,
        },
    )
    customer_comment_or_ship_comment: None | CustomerComment | ShipComment = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "customerComment",
                        "type": CustomerComment,
                        "namespace": "http://www.example.com/IPO",
                    },
                    {
                        "name": "shipComment",
                        "type": ShipComment,
                        "namespace": "http://www.example.com/IPO",
                    },
                ),
            },
        )
    )
    items: ItemsType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
            "required": True,
        }
    )
    order_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "orderDate",
            "type": "Attribute",
            "namespace": "http://www.example.com/IPO",
        },
    )

    @dataclass(kw_only=True)
    class ShipTo(AddressType):
        pass

    @dataclass(kw_only=True)
    class BillTo(AddressType):
        pass

    @dataclass(kw_only=True)
    class SingleAddress(AddressType):
        pass


@dataclass(kw_only=True)
class PurchaseOrder(PurchaseOrderType):
    class Meta:
        name = "purchaseOrder"
        namespace = "http://www.example.com/IPO"
