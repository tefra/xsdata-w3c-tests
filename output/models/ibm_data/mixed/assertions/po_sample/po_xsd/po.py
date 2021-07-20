from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from output.models.ibm_data.mixed.assertions.po_sample.po_xsd.product import Poitems


@dataclass
class Address:
    class Meta:
        name = "ADDRESS"

    street1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    street2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 3,
            "max_length": 30,
        }
    )
    zipcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 3,
            "max_length": 30,
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 3,
            "max_length": 30,
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 3,
            "max_length": 30,
        }
    )


@dataclass
class Buyer:
    class Meta:
        name = "BUYER"

    f_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fName",
            "type": "Element",
            "namespace": "",
        }
    )
    middl_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "middlName",
            "type": "Element",
            "namespace": "",
        }
    )
    l_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "lName",
            "type": "Element",
            "namespace": "",
        }
    )
    establishment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Establishment",
            "type": "Element",
            "namespace": "",
        }
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
        }
    )
    billing_address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "billing-address",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    shipping_address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "shipping-address",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r".*@.*\..*",
        }
    )
    items: Optional[Poitems] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tax: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
        }
    )
    bill_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "bill-amount",
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Order(Order1):
    class Meta:
        name = "order"
