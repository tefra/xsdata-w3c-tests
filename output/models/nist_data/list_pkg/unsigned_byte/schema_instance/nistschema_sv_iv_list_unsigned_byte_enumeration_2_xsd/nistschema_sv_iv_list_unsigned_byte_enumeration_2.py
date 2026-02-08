from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedByte-enumeration-2-NS"


class NistschemaSvIvListUnsignedByteEnumeration2Type(Enum):
    VALUE_255_40_95_70_30_41 = (
        255,
        40,
        95,
        70,
        30,
        41,
    )
    VALUE_2_3_1_52_84_98 = (
        2,
        3,
        1,
        52,
        84,
        98,
    )
    VALUE_68_3_255_29_7_48_28_66 = (
        68,
        3,
        255,
        29,
        7,
        48,
        28,
        66,
    )
    VALUE_14_28_184_73_42_255_97_80_17 = (
        14,
        28,
        184,
        73,
        42,
        255,
        97,
        80,
        17,
    )
    VALUE_13_79_255_40_6_95_197_48 = (
        13,
        79,
        255,
        40,
        6,
        95,
        197,
        48,
    )
    VALUE_255_8_3_59_49_62 = (
        255,
        8,
        3,
        59,
        49,
        62,
    )
    VALUE_134_71_5_52_8_255_18_24 = (
        134,
        71,
        5,
        52,
        8,
        255,
        18,
        24,
    )
    VALUE_10_255_3_59_47_19_126_45 = (
        10,
        255,
        3,
        59,
        47,
        19,
        126,
        45,
    )
    VALUE_255_3_87_4_82_248 = (
        255,
        3,
        87,
        4,
        82,
        248,
    )
    VALUE_10_3_255_81_140_92_22_83 = (
        10,
        3,
        255,
        81,
        140,
        92,
        22,
        83,
    )


@dataclass(kw_only=True)
class NistschemaSvIvListUnsignedByteEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedByte-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-unsignedByte-enumeration-2-NS"

    value: NistschemaSvIvListUnsignedByteEnumeration2Type = field()
