from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

__NAMESPACE__ = "tns"


class CountryType(Enum):
    """
    :cvar US:
    :cvar CAN:
    """
    US = "us"
    CAN = "can"


@dataclass
class AddressType:
    """
    :ivar any_element:
    :ivar type:
    :ivar country:
    """
    class Meta:
        name = "addressType"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: Optional["AddressType.Type"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    country: Optional[CountryType] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Type(Enum):
        """
        :cvar BILLING:
        :cvar SHIPPING:
        """
        BILLING = "billing"
        SHIPPING = "shipping"


@dataclass
class CanaddressType(AddressType):
    """
    :ivar content:
    :ivar province:
    :ivar currency:
    :ivar postal:
    """
    class Meta:
        name = "canaddressType"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    province: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
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
    postal: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True,
            pattern=r"([A-Z]\d){3}"
        )
    )


@dataclass
class UsaddressType(AddressType):
    """
    :ivar content:
    :ivar state:
    :ivar currency:
    :ivar zip:
    """
    class Meta:
        name = "usaddressType"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    state: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
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
    zip: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class ItemType:
    """
    :ivar address:
    """
    class Meta:
        name = "itemType"

    address: List[Union[AddressType, CanaddressType, UsaddressType]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Invoice:
    """
    :ivar item:
    """
    class Meta:
        name = "invoice"
        namespace = "tns"

    item: List[ItemType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
