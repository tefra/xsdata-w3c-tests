from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.complex_type.ct_z007_a_xsd.ct_z007_b import (
    CustomerType,
    PhoneNumber,
)

__NAMESPACE__ = "urn:xmlns:25hoursaday-com:address"


@dataclass
class Address:
    """
    :ivar value:
    """
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class City:
    """
    :ivar value:
    """
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class State:
    """
    :ivar value:
    """
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Zip:
    """
    :ivar value:
    """
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            pattern=r"\d{5}(-\d{4})?"
        )
    )


@dataclass
class MyCustomerType(CustomerType):
    """
    :ivar phone_number:
    :ivar address:
    :ivar city:
    :ivar state:
    :ivar zip:
    """
    phone_number: Optional[PhoneNumber] = field(
        default=None,
        metadata=dict(
            name="PhoneNumber",
            type="Element",
            namespace="urn:xmlns:25hoursaday-com:customer",
            required=True
        )
    )
    address: Optional[Address] = field(
        default=None,
        metadata=dict(
            name="Address",
            type="Element",
            namespace="urn:xmlns:25hoursaday-com:address",
            required=True
        )
    )
    city: Optional[City] = field(
        default=None,
        metadata=dict(
            name="City",
            type="Element",
            namespace="urn:xmlns:25hoursaday-com:address",
            required=True
        )
    )
    state: Optional[State] = field(
        default=None,
        metadata=dict(
            name="State",
            type="Element",
            namespace="urn:xmlns:25hoursaday-com:address",
            required=True
        )
    )
    zip: Optional[Zip] = field(
        default=None,
        metadata=dict(
            name="Zip",
            type="Element",
            namespace="urn:xmlns:25hoursaday-com:address",
            required=True
        )
    )


@dataclass
class MyCustomer(MyCustomerType):
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"
