from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-enumeration-2-NS"


class NistschemaSvIvAtomicDateEnumeration2Type(Enum):
    """
    :cvar VALUE_2013_10_28:
    :cvar VALUE_2009_09_16:
    :cvar VALUE_1974_02_14:
    :cvar VALUE_2027_04_22:
    :cvar VALUE_2027_07_03:
    :cvar VALUE_2001_08_03:
    :cvar VALUE_2015_12_10:
    """
    VALUE_2013_10_28 = "2013-10-28"
    VALUE_2009_09_16 = "2009-09-16"
    VALUE_1974_02_14 = "1974-02-14"
    VALUE_2027_04_22 = "2027-04-22"
    VALUE_2027_07_03 = "2027-07-03"
    VALUE_2001_08_03 = "2001-08-03"
    VALUE_2015_12_10 = "2015-12-10"


@dataclass
class NistschemaSvIvAtomicDateEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-date-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicDateEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
