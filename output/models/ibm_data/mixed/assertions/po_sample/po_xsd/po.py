from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import ForwardRef

from output.models.ibm_data.mixed.assertions.po_sample.po_xsd.product import (
    Item,
    LongItemDefn,
    ShortItemDefn,
)


@dataclass(kw_only=True)
class Address:
    class Meta:
        name = "ADDRESS"

    street1: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    street2: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    city: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 3,
            "max_length": 30,
        },
    )
    zipcode: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 3,
            "max_length": 30,
        },
    )
    state: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 3,
            "max_length": 30,
        },
    )
    country: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 3,
            "max_length": 30,
        },
    )


@dataclass(kw_only=True)
class Buyer:
    class Meta:
        name = "BUYER"

    choice: list[
        Buyer.FName | Buyer.MiddlName | Buyer.LName | Buyer.Establishment
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "fName",
                    "type": ForwardRef("Buyer.FName"),
                    "namespace": "",
                },
                {
                    "name": "middlName",
                    "type": ForwardRef("Buyer.MiddlName"),
                    "namespace": "",
                },
                {
                    "name": "lName",
                    "type": ForwardRef("Buyer.LName"),
                    "namespace": "",
                },
                {
                    "name": "Establishment",
                    "type": ForwardRef("Buyer.Establishment"),
                    "namespace": "",
                },
            ),
            "max_occurs": 3,
        },
    )

    @dataclass(kw_only=True)
    class FName:
        value: str = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class MiddlName:
        value: str = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class LName:
        value: str = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class Establishment:
        value: str = field(
            metadata={
                "required": True,
            }
        )


@dataclass(kw_only=True)
class PoBusinessRules:
    class Meta:
        name = "PO_BUSINESS_RULES"


@dataclass(kw_only=True)
class Order1(PoBusinessRules):
    class Meta:
        name = "ORDER"

    buyer: Buyer = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    billing_address: Address = field(
        metadata={
            "name": "billing-address",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    shipping_address: Address = field(
        metadata={
            "name": "shipping-address",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    email: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r".*@.*\..*",
        }
    )
    item: list[Item | ShortItemDefn | LongItemDefn] = field(
        default_factory=list,
        metadata={
            "wrapper": "items",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    tax: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
        }
    )
    bill_amount: Decimal = field(
        metadata={
            "name": "bill-amount",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
        }
    )
    currency: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Order(Order1):
    class Meta:
        name = "order"
