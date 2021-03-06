from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "urn:xmlns:25hoursaday-com:customer"


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

    value: str = field(
        init=False,
        default="WA",
    )


@dataclass
class Zip:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\d{5}(-\d{4})?",
        }
    )


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
class Customer(CustomerType):
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"


@dataclass
class MyCustomer(MyCustomerType):
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"


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
