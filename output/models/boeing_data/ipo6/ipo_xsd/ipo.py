from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import ForwardRef

from xsdata.models.datatype import XmlDate

from output.models.boeing_data.ipo6.ipo_xsd.address import Salutation
from output.models.boeing_data.ipo6.ipo_xsd.extend import ExternFirstElement
from output.models.boeing_data.ipo6.ipo_xsd.itematt import ItemShipBy

__NAMESPACE__ = "http://www.example.com/IPO"


@dataclass(kw_only=True)
class AddressType:
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
        }
    )
    street: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
        }
    )
    city: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
        }
    )


class Usstate(Enum):
    AK = "AK"
    AL = "AL"
    AR = "AR"
    CA = "CA"
    PA = "PA"


@dataclass(kw_only=True)
class Comment:
    class Meta:
        name = "comment"
        namespace = "http://www.example.com/IPO"

    value: str = field(default="")


@dataclass(kw_only=True)
class CustomerComment:
    class Meta:
        name = "customerComment"
        namespace = "http://www.example.com/IPO"

    value: str = field(default="")


@dataclass(kw_only=True)
class ShipComment:
    class Meta:
        name = "shipComment"
        namespace = "http://www.example.com/IPO"

    value: str = field(default="")


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
            }
        )
        quantity: int = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
                "max_exclusive": 100,
            }
        )
        usprice: Decimal = field(
            metadata={
                "name": "USPrice",
                "type": "Element",
                "namespace": "http://www.example.com/IPO",
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
class Ukaddress(AddressType):
    class Meta:
        name = "UKAddress"

    postcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
            "pattern": r"[A-Z]{2}\d\s\d[A-Z]{2}",
        }
    )
    export_code: int = field(
        init=False,
        default=1,
        metadata={
            "name": "exportCode",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Usaddress(AddressType):
    class Meta:
        name = "USAddress"

    state: Usstate = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
        }
    )
    zip: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
        }
    )


@dataclass(kw_only=True)
class Address(AddressType):
    class Meta:
        name = "address"
        namespace = "http://www.example.com/IPO"


@dataclass(kw_only=True)
class PurchaseOrderType:
    salutation_or_extern_first_element: (
        None | Salutation | ExternFirstElement
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "salutation",
                    "type": Salutation,
                    "namespace": "http://www.example.com/add",
                },
                {
                    "name": "ExternFirstElement",
                    "type": ExternFirstElement,
                    "namespace": "http://www.example.com/IPO",
                },
            ),
        },
    )
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
        }
    )
    order_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "orderDate",
            "type": "Attribute",
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
