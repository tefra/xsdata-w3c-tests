from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-byte-enumeration-4-NS"


class NistschemaSvIvListByteEnumeration4Type(Enum):
    VALUE_9_30_53_85_18_127_46_92 = (
        -9,
        -30,
        53,
        85,
        -18,
        127,
        -46,
        -92,
    )
    VALUE_23_128_81_127_41 = (
        23,
        -128,
        81,
        127,
        41,
    )
    VALUE_128_97_82_25_4_56_41_52_36 = (
        -128,
        -97,
        -82,
        25,
        -4,
        -56,
        41,
        52,
        -36,
    )
    VALUE_3_128_75_93_25_127 = (
        3,
        -128,
        -75,
        93,
        -25,
        127,
    )
    VALUE_127_9_20_46_55_97_79_60 = (
        127,
        9,
        20,
        -46,
        -55,
        -97,
        79,
        60,
    )
    VALUE_4_95_72_83_65_127_16_94 = (
        4,
        95,
        72,
        83,
        65,
        127,
        -16,
        94,
    )
    VALUE_5_88_29_127_128_91 = (
        5,
        -88,
        -29,
        127,
        -128,
        91,
    )
    VALUE_128_91_127_40_30_7_5 = (
        -128,
        -91,
        127,
        40,
        30,
        -7,
        -5,
    )


@dataclass(kw_only=True)
class NistschemaSvIvListByteEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-byte-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-byte-enumeration-4-NS"

    value: NistschemaSvIvListByteEnumeration4Type = field()
