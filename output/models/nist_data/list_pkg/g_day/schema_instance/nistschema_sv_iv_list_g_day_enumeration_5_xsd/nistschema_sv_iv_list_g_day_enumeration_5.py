from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-enumeration-5-NS"


class NistschemaSvIvListGDayEnumeration5Type(Enum):
    """
    :cvar VALUE_25_07_16_11_11_23_19:
    :cvar VALUE_26_28_21_11_16_02_03_25:
    :cvar VALUE_30_24_06_08_30_23_02:
    :cvar VALUE_12_25_26_29_13_24_26_01_26:
    :cvar VALUE_24_16_12_07_10_27_18_28:
    :cvar VALUE_18_10_19_18_06_21_17_14_17_22:
    """
    VALUE_25_07_16_11_11_23_19 = "---25 ---07 ---16 ---11 ---11 ---23 ---19"
    VALUE_26_28_21_11_16_02_03_25 = "---26 ---28 ---21 ---11 ---16 ---02 ---03 ---25"
    VALUE_30_24_06_08_30_23_02 = "---30 ---24 ---06 ---08 ---30 ---23 ---02"
    VALUE_12_25_26_29_13_24_26_01_26 = "---12 ---25 ---26 ---29 ---13 ---24 ---26 ---01 ---26"
    VALUE_24_16_12_07_10_27_18_28 = "---24 ---16 ---12 ---07 ---10 ---27 ---18 ---28"
    VALUE_18_10_19_18_06_21_17_14_17_22 = "---18 ---10 ---19 ---18 ---06 ---21 ---17 ---14 ---17 ---22"


@dataclass
class NistschemaSvIvListGDayEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-gDay-enumeration-5-NS"

    value: Optional[NistschemaSvIvListGDayEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
