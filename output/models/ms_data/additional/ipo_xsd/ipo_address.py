from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.example.com/IPO"


@dataclass
class Address:
    """
    :ivar name:
    :ivar street:
    :ivar city:
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    street: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


class Usstate(Enum):
    """
    :cvar AK:
    :cvar AL:
    :cvar AR:
    :cvar PA:
    """
    AK = "AK"
    AL = "AL"
    AR = "AR"
    PA = "PA"


@dataclass
class Ukaddress(Address):
    """
    :ivar postcode:
    :ivar export_code:
    """
    class Meta:
        name = "UKAddress"

    postcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
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
        }
    )


@dataclass
class Usaddress(Address):
    """
    :ivar state:
    :ivar zip:
    """
    class Meta:
        name = "USAddress"

    state: Optional[Usstate] = field(
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
