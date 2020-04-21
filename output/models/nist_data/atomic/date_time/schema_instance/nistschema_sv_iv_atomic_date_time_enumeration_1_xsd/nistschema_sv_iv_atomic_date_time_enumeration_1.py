from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-enumeration-1-NS"


class NistschemaSvIvAtomicDateTimeEnumeration1Type(Enum):
    """
    :cvar VALUE_1972_11_27_T20_41_04:
    :cvar VALUE_2010_02_12_T03_22_00:
    :cvar VALUE_2011_05_07_T03_49_38:
    :cvar VALUE_2015_08_04_T06_44_16:
    :cvar VALUE_2029_04_19_T14_21_30:
    :cvar VALUE_2029_12_13_T21_03_46:
    """
    VALUE_1972_11_27_T20_41_04 = "1972-11-27T20:41:04"
    VALUE_2010_02_12_T03_22_00 = "2010-02-12T03:22:00"
    VALUE_2011_05_07_T03_49_38 = "2011-05-07T03:49:38"
    VALUE_2015_08_04_T06_44_16 = "2015-08-04T06:44:16"
    VALUE_2029_04_19_T14_21_30 = "2029-04-19T14:21:30"
    VALUE_2029_12_13_T21_03_46 = "2029-12-13T21:03:46"


@dataclass
class NistschemaSvIvAtomicDateTimeEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicDateTimeEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
