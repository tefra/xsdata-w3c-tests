from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-enumeration-2-NS"


class NistschemaSvIvListGDayEnumeration2Type(Enum):
    """
    :cvar VALUE_25_19_22_06_06_20_04:
    :cvar VALUE_25_05_15_08_06_09_26_10_12_15:
    :cvar VALUE_20_15_03_11_06_27_12_18:
    :cvar VALUE_25_01_05_06_14_11_24_19:
    :cvar VALUE_29_29_20_16_19_26:
    """
    VALUE_25_19_22_06_06_20_04 = "---25 ---19 ---22 ---06 ---06 ---20 ---04"
    VALUE_25_05_15_08_06_09_26_10_12_15 = "---25 ---05 ---15 ---08 ---06 ---09 ---26 ---10 ---12 ---15"
    VALUE_20_15_03_11_06_27_12_18 = "---20 ---15 ---03 ---11 ---06 ---27 ---12 ---18"
    VALUE_25_01_05_06_14_11_24_19 = "---25 ---01 ---05 ---06 ---14 ---11 ---24 ---19"
    VALUE_29_29_20_16_19_26 = "---29 ---29 ---20 ---16 ---19 ---26"


@dataclass
class NistschemaSvIvListGDayEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-gDay-enumeration-2-NS"

    value: Optional[NistschemaSvIvListGDayEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
