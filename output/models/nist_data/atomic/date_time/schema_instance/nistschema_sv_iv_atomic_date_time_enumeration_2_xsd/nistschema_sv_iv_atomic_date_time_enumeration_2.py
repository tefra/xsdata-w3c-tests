from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-enumeration-2-NS"


class NistschemaSvIvAtomicDateTimeEnumeration2Type(Enum):
    """
    :cvar VALUE_2016_12_24_T10_20_27:
    :cvar VALUE_2013_04_14_T17_20_13:
    :cvar VALUE_1997_07_18_T03_59_37:
    :cvar VALUE_2004_04_06_T20_47_16:
    :cvar VALUE_2024_07_02_T09_44_13:
    :cvar VALUE_1980_08_25_T23_48_17:
    """
    VALUE_2016_12_24_T10_20_27 = "2016-12-24T10:20:27"
    VALUE_2013_04_14_T17_20_13 = "2013-04-14T17:20:13"
    VALUE_1997_07_18_T03_59_37 = "1997-07-18T03:59:37"
    VALUE_2004_04_06_T20_47_16 = "2004-04-06T20:47:16"
    VALUE_2024_07_02_T09_44_13 = "2024-07-02T09:44:13"
    VALUE_1980_08_25_T23_48_17 = "1980-08-25T23:48:17"


@dataclass
class NistschemaSvIvAtomicDateTimeEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicDateTimeEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
