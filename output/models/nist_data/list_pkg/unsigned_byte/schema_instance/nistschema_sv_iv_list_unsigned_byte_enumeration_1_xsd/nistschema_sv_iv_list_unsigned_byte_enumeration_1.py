from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedByte-enumeration-1-NS"


class NistschemaSvIvListUnsignedByteEnumeration1Type(Enum):
    VALUE_70_30_77_255_50_126 = (
            70,
            30,
            77,
            255,
            50,
            126,
        )
    VALUE_2_255_22_52_45_94_87 = (
            2,
            255,
            22,
            52,
            45,
            94,
            87,
        )
    VALUE_2_81_255_91_96_47_82_50_57 = (
            2,
            81,
            255,
            91,
            96,
            47,
            82,
            50,
            57,
        )
    VALUE_66_255_83_68_151_12_21_77_75 = (
            66,
            255,
            83,
            68,
            151,
            12,
            21,
            77,
            75,
        )
    VALUE_4_68_32_255_127_98 = (
            4,
            68,
            32,
            255,
            127,
            98,
        )
    VALUE_59_255_76_68_10_40_69_79_34 = (
            59,
            255,
            76,
            68,
            10,
            40,
            69,
            79,
            34,
        )
    VALUE_25_18_255_48_7_163_92_76 = (
            25,
            18,
            255,
            48,
            7,
            163,
            92,
            76,
        )
    VALUE_255_79_42_52_6_47 = (
            255,
            79,
            42,
            52,
            6,
            47,
        )


@dataclass
class NistschemaSvIvListUnsignedByteEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedByte-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-unsignedByte-enumeration-1-NS"

    value: Optional[NistschemaSvIvListUnsignedByteEnumeration1Type] = field(
        default=None
    )
