from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.complex_type.ct_z007_a_xsd.ct_z007_a import MyCustomer

__NAMESPACE__ = "urn:xmlns:25hoursaday-com:customer"


@dataclass
class CustomerType:
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:customer",
            "required": True,
        }
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastName",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:customer",
            "required": True,
        }
    )
    customer_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "customerID",
            "type": "Attribute",
        }
    )


@dataclass
class FirstName:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class LastName:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PhoneNumber:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Customer(CustomerType):
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"


@dataclass
class Customers:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"

    my_customer: List[MyCustomer] = field(
        default_factory=list,
        metadata={
            "name": "MyCustomer",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:address",
            "min_occurs": 1,
        }
    )
    customer: List[Customer] = field(
        default_factory=list,
        metadata={
            "name": "Customer",
            "type": "Element",
            "min_occurs": 1,
        }
    )
