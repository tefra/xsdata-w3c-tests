from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-byte-enumeration-2-NS"


class NistschemaSvIvListByteEnumeration2Type(Enum):
    VALUE_85_61_24_4_127_46_33_67_59 = (
            85,
            -61,
            24,
            -4,
            127,
            -46,
            33,
            -67,
            59,
        )
    VALUE_128_35_2_79_8_43_40_127 = (
            -128,
            -35,
            -2,
            -79,
            -8,
            43,
            -40,
            127,
        )
    VALUE_59_127_128_85_54_5 = (
            59,
            127,
            -128,
            85,
            54,
            -5,
        )
    VALUE_40_38_79_51_84_48_4 = (
            40,
            38,
            79,
            51,
            84,
            48,
            -4,
        )
    VALUE_45_46_80_5_51_128_74_15 = (
            45,
            46,
            80,
            -5,
            51,
            -128,
            74,
            15,
        )


@dataclass
class NistschemaSvIvListByteEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-byte-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-byte-enumeration-2-NS"

    value: Optional[NistschemaSvIvListByteEnumeration2Type] = field(
        default=None
    )
