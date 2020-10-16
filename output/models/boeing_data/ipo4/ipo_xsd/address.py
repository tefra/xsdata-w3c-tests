from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from output.models.boeing_data.ipo4.ipo_xsd.ipo import AddressType

__NAMESPACE__ = "http://www.example.com/IPO"


class Usstate(Enum):
    """
    :cvar AK:
    :cvar AL:
    :cvar AR:
    :cvar CA:
    :cvar PA:
    """
    AK = "AK"
    AL = "AL"
    AR = "AR"
    CA = "CA"
    PA = "PA"


@dataclass
class Ukaddress(AddressType):
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
class Usaddress(AddressType):
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
