from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-enumeration-1-NS"


class NistschemaSvIvListGDayEnumeration1Type(Enum):
    """
    :cvar VALUE_17_30_09_01_05_09_09_30:
    :cvar VALUE_21_30_16_07_18_25_02:
    :cvar VALUE_26_04_07_18_19:
    :cvar VALUE_13_16_08_16_04:
    :cvar VALUE_23_20_28_28_07_09_25_11_06:
    """
    VALUE_17_30_09_01_05_09_09_30 = "---17 ---30 ---09 ---01 ---05 ---09 ---09 ---30"
    VALUE_21_30_16_07_18_25_02 = "---21 ---30 ---16 ---07 ---18 ---25 ---02"
    VALUE_26_04_07_18_19 = "---26 ---04 ---07 ---18 ---19"
    VALUE_13_16_08_16_04 = "---13 ---16 ---08 ---16 ---04"
    VALUE_23_20_28_28_07_09_25_11_06 = "---23 ---20 ---28 ---28 ---07 ---09 ---25 ---11 ---06"


@dataclass
class NistschemaSvIvListGDayEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-gDay-enumeration-1-NS"

    value: Optional[NistschemaSvIvListGDayEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
