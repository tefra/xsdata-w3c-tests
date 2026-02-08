from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDate

from output.models.ms_data.additional.ipo_xsd.ipo_address import Address

__NAMESPACE__ = "http://www.example.com/IPO"


@dataclass(kw_only=True)
class Comment:
    class Meta:
        name = "comment"
        namespace = "http://www.example.com/IPO"

    value: str = field(default="")


@dataclass(kw_only=True)
class Items:
    item: list[Items.Item] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass(kw_only=True)
    class Item:
        product_name: str = field(
            metadata={
                "name": "productName",
                "type": "Element",
                "namespace": "",
            }
        )
        quantity: int = field(
            metadata={
                "type": "Element",
                "namespace": "",
                "max_exclusive": 100,
            }
        )
        usprice: Decimal = field(
            metadata={
                "name": "USPrice",
                "type": "Element",
                "namespace": "",
            }
        )
        comment: None | Comment = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
            },
        )
        ship_date: None | XmlDate = field(
            default=None,
            metadata={
                "name": "shipDate",
                "type": "Element",
                "namespace": "",
            },
        )
        part_num: str = field(
            metadata={
                "name": "partNum",
                "type": "Attribute",
                "pattern": r"\d{3}-[A-Z]{2}",
            }
        )


@dataclass(kw_only=True)
class PurchaseOrderType:
    ship_to: Address = field(
        metadata={
            "name": "shipTo",
            "type": "Element",
            "namespace": "",
        }
    )
    bill_to: None | Address = field(
        default=None,
        metadata={
            "name": "billTo",
            "type": "Element",
            "namespace": "",
        },
    )
    comment: None | Comment = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
        },
    )
    items: None | Items = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    order_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "orderDate",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class PurchaseOrder(PurchaseOrderType):
    class Meta:
        name = "purchaseOrder"
        namespace = "http://www.example.com/IPO"
