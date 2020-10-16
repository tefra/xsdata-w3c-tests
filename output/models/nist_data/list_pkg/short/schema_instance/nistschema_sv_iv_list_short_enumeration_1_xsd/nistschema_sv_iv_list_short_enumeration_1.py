from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-short-enumeration-1-NS"


class NistschemaSvIvListShortEnumeration1Type(Enum):
    """
    :cvar VALUE_709_574_8877_84_8378_74_32767_824_72_30:
    :cvar VALUE_71_33_8995_657_32767_58_720_68:
    :cvar VALUE_900_4563_32768_28_99_8520:
    :cvar VALUE_917_16287_76_6691_85_4592_9064_793:
    :cvar VALUE_3203_49_36_3339_9350_14545_224_32768_969:
    :cvar VALUE_427_6_721_3593_735_401_4398_77_9600_490:
    """
    VALUE_709_574_8877_84_8378_74_32767_824_72_30 = "709 -574 8877 -84 8378 -74 32767 824 -72 30"
    VALUE_71_33_8995_657_32767_58_720_68 = "71 -33 8995 -657 32767 58 -720 68"
    VALUE_900_4563_32768_28_99_8520 = "-900 4563 -32768 -28 99 8520"
    VALUE_917_16287_76_6691_85_4592_9064_793 = "917 16287 -76 6691 -85 -4592 9064 793"
    VALUE_3203_49_36_3339_9350_14545_224_32768_969 = "3203 -49 36 3339 -9350 14545 -224 -32768 -969"
    VALUE_427_6_721_3593_735_401_4398_77_9600_490 = "427 -6 721 -3593 -735 -401 -4398 77 -9600 490"


@dataclass
class NistschemaSvIvListShortEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-short-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-short-enumeration-1-NS"

    value: Optional[NistschemaSvIvListShortEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
