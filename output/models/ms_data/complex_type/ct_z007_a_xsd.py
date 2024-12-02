from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Address:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class City:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class State:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: str = field(
        init=False,
        default="WA",
        metadata={
            "required": True,
        },
    )


@dataclass
class Zip:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d{5}(-\d{4})?",
        },
    )


@dataclass
class FirstName:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class LastName:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class PhoneNumber:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class CustomerType:
    class Meta:
        target_namespace = "urn:xmlns:25hoursaday-com:customer"

    first_name: Optional[FirstName] = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:customer",
            "required": True,
        },
    )
    last_name: Optional[LastName] = field(
        default=None,
        metadata={
            "name": "LastName",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:customer",
            "required": True,
        },
    )
    customer_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "customerID",
            "type": "Attribute",
        },
    )


@dataclass
class MyCustomerType(CustomerType):
    class Meta:
        target_namespace = "urn:xmlns:25hoursaday-com:address"

    phone_number: Optional[PhoneNumber] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:customer",
            "required": True,
        },
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:address",
            "required": True,
        },
    )
    city: Optional[City] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:address",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:address",
            "required": True,
        },
    )
    zip: Optional[Zip] = field(
        default=None,
        metadata={
            "name": "Zip",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:address",
            "required": True,
        },
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

    my_customer: list[MyCustomer] = field(
        default_factory=list,
        metadata={
            "name": "MyCustomer",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:address",
        },
    )
