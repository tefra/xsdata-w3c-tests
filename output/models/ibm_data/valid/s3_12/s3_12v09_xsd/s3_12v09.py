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

    type_value: Optional[AddressTypeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        }
    )
    country: Optional[CountryType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class CanaddressType(AddressType):
    class Meta:
        name = "canaddressType"


@dataclass
class UsaddressType(AddressType):
    class Meta:
        name = "usaddressType"


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
