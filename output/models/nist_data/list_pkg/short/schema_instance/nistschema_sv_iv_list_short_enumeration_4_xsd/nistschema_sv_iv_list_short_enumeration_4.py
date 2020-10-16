from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-short-enumeration-4-NS"


class NistschemaSvIvListShortEnumeration4Type(Enum):
    """
    :cvar VALUE_9006_8125_8712_28752_556_32767_41:
    :cvar VALUE_1825_32767_98_9644_84_9340_8_74_23:
    :cvar VALUE_667_257_613_48_76_173_3691_469:
    :cvar VALUE_2723_32767_821_3906_8985_306_356:
    :cvar VALUE_9_950_201_728_5862_9551_24_3_567:
    :cvar VALUE_41_2433_2017_563_550_267:
    :cvar VALUE_32767_4388_426_6682_54_64:
    :cvar VALUE_4_314_87_63_1160_4561_158_9:
    """
    VALUE_9006_8125_8712_28752_556_32767_41 = "9006 8125 -8712 28752 556 32767 -41"
    VALUE_1825_32767_98_9644_84_9340_8_74_23 = "1825 32767 -98 -9644 84 -9340 -8 74 23"
    VALUE_667_257_613_48_76_173_3691_469 = "667 257 -613 48 -76 173 -3691 -469"
    VALUE_2723_32767_821_3906_8985_306_356 = "-2723 32767 -821 -3906 8985 -306 -356"
    VALUE_9_950_201_728_5862_9551_24_3_567 = "9 -950 201 -728 5862 9551 -24 3 567"
    VALUE_41_2433_2017_563_550_267 = "-41 -2433 2017 563 550 267"
    VALUE_32767_4388_426_6682_54_64 = "32767 -4388 426 6682 54 -64"
    VALUE_4_314_87_63_1160_4561_158_9 = "-4 314 87 -63 -1160 -4561 158 -9"


@dataclass
class NistschemaSvIvListShortEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-short-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-short-enumeration-4-NS"

    value: Optional[NistschemaSvIvListShortEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
