from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "http://www.example.com/add"


@dataclass(kw_only=True)
class AddressType:
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    street: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    city: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


class Usstate(Enum):
    AK = "AK"
    AL = "AL"
    AR = "AR"
    CA = "CA"
    PA = "PA"


@dataclass(kw_only=True)
class Ukaddress(AddressType):
    class Meta:
        name = "UKAddress"

    postcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[A-Z]{2}\d\s\d[A-Z]{2}",
        }
    )
    export_code: int = field(
        init=False,
        default=1,
        metadata={
            "name": "exportCode",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Usaddress(AddressType):
    class Meta:
        name = "USAddress"

    state: Usstate = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    zip: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
