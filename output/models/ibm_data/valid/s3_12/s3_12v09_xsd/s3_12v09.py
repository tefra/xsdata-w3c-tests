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
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    type: Optional["AddressType.Type"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    country: Optional[CountryType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    province: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
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
    postal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"([A-Z]\d){3}",
        }
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
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
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
    zip: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
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
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
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
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
