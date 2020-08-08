from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional
from output.models.ibm_data.mixed.assertions.po_sample.po_xsd.product import Poitems


@dataclass
class Address:
    """
    :ivar street1:
    :ivar street2:
    :ivar city:
    :ivar zipcode:
    :ivar state:
    :ivar country:
    """
    class Meta:
        name = "ADDRESS"

    street1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    street2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    city: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            min_length=3,
            max_length=30
        )
    )
    zipcode: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            min_length=3,
            max_length=30
        )
    )
    state: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            min_length=3,
            max_length=30
        )
    )
    country: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            min_length=3,
            max_length=30
        )
    )


@dataclass
class Buyer:
    """
    :ivar f_name:
    :ivar middl_name:
    :ivar l_name:
    :ivar establishment:
    """
    class Meta:
        name = "BUYER"

    f_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="fName",
            type="Element",
            namespace="",
            required=True
        )
    )
    middl_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="middlName",
            type="Element",
            namespace=""
        )
    )
    l_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="lName",
            type="Element",
            namespace="",
            required=True
        )
    )
    establishment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Establishment",
            type="Element",
            namespace=""
        )
    )


@dataclass
class PoBusinessRules:
    class Meta:
        name = "PO_BUSINESS_RULES"


@dataclass
class Order(PoBusinessRules):
    """
    :ivar buyer:
    :ivar billing_address:
    :ivar shipping_address:
    :ivar email:
    :ivar items:
    :ivar tax:
    :ivar bill_amount:
    :ivar currency:
    :ivar id:
    """
    class Meta:
        name = "ORDER"

    buyer: Optional[Buyer] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    billing_address: Optional[Address] = field(
        default=None,
        metadata=dict(
            name="billing-address",
            type="Element",
            namespace="",
            required=True
        )
    )
    shipping_address: Optional[Address] = field(
        default=None,
        metadata=dict(
            name="shipping-address",
            type="Element",
            namespace="",
            required=True
        )
    )
    email: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True,
            pattern=r".*@.*\..*"
        )
    )
    items: Optional[Poitems] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    tax: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True,
            min_inclusive=0
        )
    )
    bill_amount: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="bill-amount",
            type="Element",
            namespace="",
            required=True,
            min_inclusive=0
        )
    )
    currency: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class Order(Order):
    class Meta:
        name = "order"
