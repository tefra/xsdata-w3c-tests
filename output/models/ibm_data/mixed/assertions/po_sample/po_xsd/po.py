from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Type, Union

from output.models.ibm_data.mixed.assertions.po_sample.po_xsd.product import (
    Poitems,
)


@dataclass
class Address:
    class Meta:
        name = "ADDRESS"

    street1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    street2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 3,
            "max_length": 30,
        },
    )
    zipcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 3,
            "max_length": 30,
        },
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 3,
            "max_length": 30,
        },
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 3,
            "max_length": 30,
        },
    )


@dataclass
class Buyer:
    class Meta:
        name = "BUYER"

    choice: List[
        Union[
            "Buyer.FName",
            "Buyer.MiddlName",
            "Buyer.LName",
            "Buyer.Establishment",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "fName",
                    "type": Type["Buyer.FName"],
                    "namespace": "",
                },
                {
                    "name": "middlName",
                    "type": Type["Buyer.MiddlName"],
                    "namespace": "",
                },
                {
                    "name": "lName",
                    "type": Type["Buyer.LName"],
                    "namespace": "",
                },
                {
                    "name": "Establishment",
                    "type": Type["Buyer.Establishment"],
                    "namespace": "",
                },
            ),
            "max_occurs": 3,
        },
    )

    @dataclass
    class FName:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class MiddlName:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class LName:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Establishment:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class PoBusinessRules:
    class Meta:
        name = "PO_BUSINESS_RULES"


@dataclass
class Order1(PoBusinessRules):
    class Meta:
        name = "ORDER"

    buyer: Optional[Buyer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    billing_address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "billing-address",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    shipping_address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "shipping-address",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r".*@.*\..*",
        },
    )
    items: Optional[Poitems] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    tax: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
        },
    )
    bill_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "bill-amount",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
        },
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Order(Order1):
    class Meta:
        name = "order"
