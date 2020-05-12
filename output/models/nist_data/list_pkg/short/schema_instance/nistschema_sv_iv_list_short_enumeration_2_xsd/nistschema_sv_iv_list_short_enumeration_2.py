from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-short-enumeration-2-NS"


class NistschemaSvIvListShortEnumeration2Type(Enum):
    """
    :cvar VALUE_626_2215_58_32767_5279_6265_42_534:
    :cvar VALUE_491_8628_2246_488_627:
    :cvar VALUE_9188_29_43_47_8_95_25_32768:
    :cvar VALUE_15_4002_70_85_793_22_20_55_6567:
    :cvar VALUE_25_7477_32768_7364_2002_1_3208_19:
    :cvar VALUE_19_89_4924_67_930_15_7:
    :cvar VALUE_829_411_7673_68_2477_3760_11:
    :cvar VALUE_125_22_871_9045_5012_8684_547:
    :cvar VALUE_79_826_288_49_869_32767_32768_50:
    """
    VALUE_626_2215_58_32767_5279_6265_42_534 = "-626 2215 58 32767 5279 6265 42 -534"
    VALUE_491_8628_2246_488_627 = "491 -8628 2246 -488 627"
    VALUE_9188_29_43_47_8_95_25_32768 = "-9188 -29 -43 47 -8 95 25 -32768"
    VALUE_15_4002_70_85_793_22_20_55_6567 = "15 4002 -70 -85 -793 22 20 55 -6567"
    VALUE_25_7477_32768_7364_2002_1_3208_19 = "25 -7477 -32768 -7364 2002 -1 3208 19"
    VALUE_19_89_4924_67_930_15_7 = "19 89 4924 -67 930 -15 -7"
    VALUE_829_411_7673_68_2477_3760_11 = "-829 411 -7673 -68 -2477 -3760 -11"
    VALUE_125_22_871_9045_5012_8684_547 = "-125 22 -871 -9045 5012 -8684 547"
    VALUE_79_826_288_49_869_32767_32768_50 = "79 -826 288 49 -869 32767 -32768 -50"


@dataclass
class NistschemaSvIvListShortEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-short-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-short-enumeration-2-NS"

    value: Optional[NistschemaSvIvListShortEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
