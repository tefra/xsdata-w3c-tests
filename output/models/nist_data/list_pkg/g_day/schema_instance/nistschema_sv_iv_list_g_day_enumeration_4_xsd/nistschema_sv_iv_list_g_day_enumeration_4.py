from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-enumeration-4-NS"


class NistschemaSvIvListGDayEnumeration4Type(Enum):
    """
    :cvar VALUE_03_10_23_15_04_12:
    :cvar VALUE_08_02_19_29_19_03_22_03:
    :cvar VALUE_14_08_22_25_18:
    :cvar VALUE_16_02_07_15_27_01_02_17:
    :cvar VALUE_27_19_10_22_13:
    :cvar VALUE_28_25_05_23_14_05_25:
    """
    VALUE_03_10_23_15_04_12 = "---03 ---10 ---23 ---15 ---04 ---12"
    VALUE_08_02_19_29_19_03_22_03 = "---08 ---02 ---19 ---29 ---19 ---03 ---22 ---03"
    VALUE_14_08_22_25_18 = "---14 ---08 ---22 ---25 ---18"
    VALUE_16_02_07_15_27_01_02_17 = "---16 ---02 ---07 ---15 ---27 ---01 ---02 ---17"
    VALUE_27_19_10_22_13 = "---27 ---19 ---10 ---22 ---13"
    VALUE_28_25_05_23_14_05_25 = "---28 ---25 ---05 ---23 ---14 ---05 ---25"


@dataclass
class NistschemaSvIvListGDayEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-gDay-enumeration-4-NS"

    value: Optional[NistschemaSvIvListGDayEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )