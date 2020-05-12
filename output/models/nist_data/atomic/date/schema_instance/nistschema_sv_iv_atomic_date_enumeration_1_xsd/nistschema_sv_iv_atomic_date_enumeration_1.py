from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-enumeration-1-NS"


class NistschemaSvIvAtomicDateEnumeration1Type(Enum):
    """
    :cvar VALUE_1975_06_11:
    :cvar VALUE_1997_12_26:
    :cvar VALUE_1998_11_16:
    :cvar VALUE_2023_08_17:
    :cvar VALUE_2010_04_24:
    :cvar VALUE_2028_06_23:
    :cvar VALUE_2015_03_13:
    :cvar VALUE_2026_01_04:
    """
    VALUE_1975_06_11 = "1975-06-11"
    VALUE_1997_12_26 = "1997-12-26"
    VALUE_1998_11_16 = "1998-11-16"
    VALUE_2023_08_17 = "2023-08-17"
    VALUE_2010_04_24 = "2010-04-24"
    VALUE_2028_06_23 = "2028-06-23"
    VALUE_2015_03_13 = "2015-03-13"
    VALUE_2026_01_04 = "2026-01-04"


@dataclass
class NistschemaSvIvAtomicDateEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-date-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicDateEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
