from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.complex_type.ct_z007_a_xsd.ct_z007_b import CustomerType

__NAMESPACE__ = "urn:xmlns:25hoursaday-com:address"


@dataclass
class Address:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class City:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class State:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Zip:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"\d{5}(-\d{4})?",
        }
    )


@dataclass
class MyCustomerType(CustomerType):
    phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:customer",
            "required": True,
        }
    )
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:address",
            "required": True,
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:address",
            "required": True,
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:address",
            "required": True,
        }
    )
    zip: Optional[str] = field(
        default=None,
        metadata={
            "name": "Zip",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:address",
            "required": True,
            "pattern": r"\d{5}(-\d{4})?",
        }
    )


@dataclass
class MyCustomer(MyCustomerType):
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"
