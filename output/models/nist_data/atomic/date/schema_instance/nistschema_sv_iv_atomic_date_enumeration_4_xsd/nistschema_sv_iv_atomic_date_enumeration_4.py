from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-enumeration-4-NS"


class NistschemaSvIvAtomicDateEnumeration4Type(Enum):
    """
    :cvar VALUE_1991_09_06:
    :cvar VALUE_2022_07_25:
    :cvar VALUE_2021_10_20:
    :cvar VALUE_1984_08_15:
    :cvar VALUE_1975_11_02:
    :cvar VALUE_2000_02_01:
    """
    VALUE_1991_09_06 = "1991-09-06"
    VALUE_2022_07_25 = "2022-07-25"
    VALUE_2021_10_20 = "2021-10-20"
    VALUE_1984_08_15 = "1984-08-15"
    VALUE_1975_11_02 = "1975-11-02"
    VALUE_2000_02_01 = "2000-02-01"


@dataclass
class NistschemaSvIvAtomicDateEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-date-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicDateEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
