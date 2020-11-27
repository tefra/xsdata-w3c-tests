from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-enumeration-4-NS"


class NistschemaSvIvListGDayEnumeration4Type(Enum):
    VALUE_03_10_23_15_04_12 = "---03 ---10 ---23 ---15 ---04 ---12"
    VALUE_28_25_05_23_14_05_25 = "---28 ---25 ---05 ---23 ---14 ---05 ---25"
    VALUE_08_02_19_29_19_03_22_03 = "---08 ---02 ---19 ---29 ---19 ---03 ---22 ---03"
    VALUE_16_02_07_15_27_01_02_17 = "---16 ---02 ---07 ---15 ---27 ---01 ---02 ---17"
    VALUE_14_08_22_25_18 = "---14 ---08 ---22 ---25 ---18"
    VALUE_27_19_10_22_13 = "---27 ---19 ---10 ---22 ---13"


@dataclass
class NistschemaSvIvListGDayEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-gDay-enumeration-4-NS"

    value: Optional[NistschemaSvIvListGDayEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
