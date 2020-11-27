from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-enumeration-3-NS"


class NistschemaSvIvListGDayEnumeration3Type(Enum):
    VALUE_21_08_18_30_15_29_09_10_30_30 = "---21 ---08 ---18 ---30 ---15 ---29 ---09 ---10 ---30 ---30"
    VALUE_13_14_22_29_18_12 = "---13 ---14 ---22 ---29 ---18 ---12"
    VALUE_24_11_17_19_06_02 = "---24 ---11 ---17 ---19 ---06 ---02"
    VALUE_12_16_08_19_26_28_08_14_02_04 = "---12 ---16 ---08 ---19 ---26 ---28 ---08 ---14 ---02 ---04"
    VALUE_25_05_05_14_23_17_30 = "---25 ---05 ---05 ---14 ---23 ---17 ---30"
    VALUE_16_28_16_29_02_14 = "---16 ---28 ---16 ---29 ---02 ---14"
    VALUE_30_02_22_14_18_12_16_27 = "---30 ---02 ---22 ---14 ---18 ---12 ---16 ---27"
    VALUE_09_09_08_01_23_25_16_27_29 = "---09 ---09 ---08 ---01 ---23 ---25 ---16 ---27 ---29"
    VALUE_18_29_16_28_13_15_06_23_21 = "---18 ---29 ---16 ---28 ---13 ---15 ---06 ---23 ---21"


@dataclass
class NistschemaSvIvListGDayEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-gDay-enumeration-3-NS"

    value: Optional[NistschemaSvIvListGDayEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
