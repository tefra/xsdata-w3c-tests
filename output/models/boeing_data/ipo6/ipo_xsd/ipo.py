from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Type, Union

from xsdata.models.datatype import XmlDate

from output.models.boeing_data.ipo6.ipo_xsd.address import Salutation
from output.models.boeing_data.ipo6.ipo_xsd.extend import ExternFirstElement
from output.models.boeing_data.ipo6.ipo_xsd.itematt import ItemShipBy

__NAMESPACE__ = "http://www.example.com/IPO"


@dataclass
class AddressType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
            "required": True,
        },
    )
    street: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
            "required": True,
        },
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
            "required": True,
        },
    )


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

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


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
        customer_comment_or_ship_comment: List[
            Union[CustomerComment, ShipComment]
        ] = field(
            default_factory=list,
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
        },
    )
    export_code: int = field(
        init=False,
        default=1,
        metadata={
            "name": "exportCode",
            "type": "Attribute",
        },
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
        },
    )
    zip: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/IPO",
            "required": True,
        },
    )


@dataclass
class Address(AddressType):
    class Meta:
        name = "address"
        namespace = "http://www.example.com/IPO"


@dataclass
class PurchaseOrderType:
    salutation_or_extern_first_element: Optional[
        Union[Salutation, ExternFirstElement]
    ] = field(
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
    ship_to_or_bill_to_or_single_address: List[
        Union[
            "PurchaseOrderType.ShipTo",
            "PurchaseOrderType.BillTo",
            "PurchaseOrderType.SingleAddress",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "shipTo",
                    "type": Type["PurchaseOrderType.ShipTo"],
                    "namespace": "http://www.example.com/IPO",
                },
                {
                    "name": "billTo",
                    "type": Type["PurchaseOrderType.BillTo"],
                    "namespace": "http://www.example.com/IPO",
                },
                {
                    "name": "singleAddress",
                    "type": Type["PurchaseOrderType.SingleAddress"],
                    "namespace": "http://www.example.com/IPO",
                },
            ),
            "max_occurs": 2,
        },
    )
    customer_comment_or_ship_comment: Optional[
        Union[CustomerComment, ShipComment]
    ] = field(
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
        },
    )

    @dataclass
    class ShipTo(AddressType):
        pass

    @dataclass
    class BillTo(AddressType):
        pass

    @dataclass
    class SingleAddress(AddressType):
        pass


@dataclass
class PurchaseOrder(PurchaseOrderType):
    class Meta:
        name = "purchaseOrder"
        namespace = "http://www.example.com/IPO"
