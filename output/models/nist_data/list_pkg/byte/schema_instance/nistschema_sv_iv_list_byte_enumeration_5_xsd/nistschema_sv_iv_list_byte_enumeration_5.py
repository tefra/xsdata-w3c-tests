from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-byte-enumeration-5-NS"


class NistschemaSvIvListByteEnumeration5Type(Enum):
    VALUE_93_38_4_32_33_85_65_97 = (
        93,
        -38,
        -4,
        32,
        33,
        85,
        -65,
        -97,
    )
    VALUE_57_23_3_8_75_51_22_56 = (
        -57,
        -23,
        -3,
        -8,
        -75,
        51,
        -22,
        56,
    )
    VALUE_54_128_127_41_5 = (
        54,
        -128,
        127,
        41,
        -5,
    )
    VALUE_32_128_77_68_9_80_127_57_59_37 = (
        -32,
        -128,
        -77,
        -68,
        9,
        80,
        127,
        -57,
        59,
        37,
    )
    VALUE_88_5_2_66_128_56_62 = (
        -88,
        5,
        2,
        -66,
        -128,
        56,
        62,
    )
    VALUE_8_3_120_76_21_52_6_43_36 = (
        -8,
        3,
        120,
        76,
        -21,
        -52,
        -6,
        -43,
        36,
    )
    VALUE_28_1_88_127_54_86 = (
        -28,
        1,
        88,
        127,
        54,
        86,
    )
    VALUE_127_128_36_18_92_46 = (
        127,
        -128,
        -36,
        18,
        92,
        46,
    )


@dataclass
class NistschemaSvIvListByteEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-byte-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-byte-enumeration-5-NS"

    value: Optional[NistschemaSvIvListByteEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
