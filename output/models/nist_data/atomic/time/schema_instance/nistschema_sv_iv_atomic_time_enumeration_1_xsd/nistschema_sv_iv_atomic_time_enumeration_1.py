from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-enumeration-1-NS"


class NistschemaSvIvAtomicTimeEnumeration1Type(Enum):
    """
    :cvar VALUE_01_42_27:
    :cvar VALUE_01_44_56:
    :cvar VALUE_02_00_14:
    :cvar VALUE_02_47_45:
    :cvar VALUE_03_43_07:
    :cvar VALUE_05_55_52:
    :cvar VALUE_07_44_41:
    :cvar VALUE_12_41_23:
    :cvar VALUE_21_59_07:
    """
    VALUE_01_42_27 = "01:42:27"
    VALUE_01_44_56 = "01:44:56"
    VALUE_02_00_14 = "02:00:14"
    VALUE_02_47_45 = "02:47:45"
    VALUE_03_43_07 = "03:43:07"
    VALUE_05_55_52 = "05:55:52"
    VALUE_07_44_41 = "07:44:41"
    VALUE_12_41_23 = "12:41:23"
    VALUE_21_59_07 = "21:59:07"


@dataclass
class NistschemaSvIvAtomicTimeEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-time-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicTimeEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )