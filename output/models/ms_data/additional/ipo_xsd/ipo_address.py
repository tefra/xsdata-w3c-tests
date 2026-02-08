from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "http://www.example.com/IPO"


@dataclass(kw_only=True)
class Address:
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    street: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    city: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class Usstate(Enum):
    AK = "AK"
    AL = "AL"
    AR = "AR"
    PA = "PA"


@dataclass(kw_only=True)
class Ukaddress(Address):
    class Meta:
        name = "UKAddress"

    postcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "length": 7,
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
class Usaddress(Address):
    class Meta:
        name = "USAddress"

    state: Usstate = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    zip: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
