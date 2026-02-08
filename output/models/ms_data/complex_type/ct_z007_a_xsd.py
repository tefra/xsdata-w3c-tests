from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Address:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: str = field(default="")


@dataclass(kw_only=True)
class City:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: str = field(default="")


@dataclass(kw_only=True)
class State:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: str = field(init=False, default="WA")


@dataclass(kw_only=True)
class Zip:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d{5}(-\d{4})?",
        },
    )


@dataclass(kw_only=True)
class FirstName:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"

    value: str = field(default="")


@dataclass(kw_only=True)
class LastName:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"

    value: str = field(default="")


@dataclass(kw_only=True)
class PhoneNumber:
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"

    value: str = field(default="")


@dataclass(kw_only=True)
class CustomerType:
    class Meta:
        target_namespace = "urn:xmlns:25hoursaday-com:customer"

    first_name: FirstName = field(
        metadata={
            "name": "FirstName",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:customer",
        }
    )
    last_name: LastName = field(
        metadata={
            "name": "LastName",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:customer",
        }
    )
    customer_id: None | int = field(
        default=None,
        metadata={
            "name": "customerID",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class MyCustomerType(CustomerType):
    class Meta:
        target_namespace = "urn:xmlns:25hoursaday-com:address"

    phone_number: PhoneNumber = field(
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:customer",
        }
    )
    address: Address = field(
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:address",
        }
    )
    city: City = field(
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:address",
        }
    )
    state: State = field(
        metadata={
            "name": "State",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:address",
        }
    )
    zip: Zip = field(
        metadata={
            "name": "Zip",
            "type": "Element",
            "namespace": "urn:xmlns:25hoursaday-com:address",
        }
    )


@dataclass(kw_only=True)
class Customer(CustomerType):
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"


@dataclass(kw_only=True)
class MyCustomer(MyCustomerType):
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:address"


@dataclass(kw_only=True)
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
