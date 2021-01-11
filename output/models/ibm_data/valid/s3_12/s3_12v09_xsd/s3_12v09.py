from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

__NAMESPACE__ = "tns"


class AddressTypeType(Enum):
    BILLING = "billing"
    SHIPPING = "shipping"


class CountryType(Enum):
    US = "us"
    CAN = "can"


@dataclass
class AddressType:
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
    type: Optional[AddressTypeType] = field(
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


@dataclass
class CanaddressType(AddressType):
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
    class Meta:
        name = "itemType"

    address: List[Union[AddressType, UsaddressType, CanaddressType]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class Invoice:
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
