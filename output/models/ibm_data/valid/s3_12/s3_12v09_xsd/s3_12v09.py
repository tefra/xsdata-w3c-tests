from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "tns"


class AddressTypeType(Enum):
    BILLING = "billing"
    SHIPPING = "shipping"


class CountryType(Enum):
    US = "us"
    CAN = "can"


@dataclass(kw_only=True)
class AddressType:
    class Meta:
        name = "addressType"

    type_value: None | AddressTypeType = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    country: None | CountryType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CanaddressType(AddressType):
    class Meta:
        name = "canaddressType"


@dataclass(kw_only=True)
class UsaddressType(AddressType):
    class Meta:
        name = "usaddressType"


@dataclass(kw_only=True)
class ItemType:
    class Meta:
        name = "itemType"

    address: list[AddressType | UsaddressType | CanaddressType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Invoice:
    class Meta:
        name = "invoice"
        namespace = "tns"

    item: list[ItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
