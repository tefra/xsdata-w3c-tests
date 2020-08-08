from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.complex_type.ct_z007_a_xsd.ct_z007_a import MyCustomer

__NAMESPACE__ = "urn:xmlns:25hoursaday-com:customer"


@dataclass
class FirstName:
    """
    :ivar value:
    """
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class LastName:
    """
    :ivar value:
    """
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class PhoneNumber:
    """
    :ivar value:
    """
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class CustomerType:
    """
    :ivar first_name:
    :ivar last_name:
    :ivar customer_id:
    """
    first_name: Optional[FirstName] = field(
        default=None,
        metadata=dict(
            name="FirstName",
            type="Element",
            namespace="urn:xmlns:25hoursaday-com:customer",
            required=True
        )
    )
    last_name: Optional[LastName] = field(
        default=None,
        metadata=dict(
            name="LastName",
            type="Element",
            namespace="urn:xmlns:25hoursaday-com:customer",
            required=True
        )
    )
    customer_id: Optional[int] = field(
        default=None,
        metadata=dict(
            name="customerID",
            type="Attribute"
        )
    )


@dataclass
class Customer(CustomerType):
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"


@dataclass
class Customers:
    """
    :ivar my_customer:
    :ivar customer:
    """
    class Meta:
        namespace = "urn:xmlns:25hoursaday-com:customer"

    my_customer: List[MyCustomer] = field(
        default_factory=list,
        metadata=dict(
            name="MyCustomer",
            type="Element",
            namespace="urn:xmlns:25hoursaday-com:address",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    customer: List[Customer] = field(
        default_factory=list,
        metadata=dict(
            name="Customer",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
