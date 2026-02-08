from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-short-enumeration-5-NS"


class NistschemaSvIvListShortEnumeration5Type(Enum):
    VALUE_291_19_61_758_799_4158 = (
        -291,
        -19,
        61,
        -758,
        799,
        -4158,
    )
    VALUE_874_32767_88_872_7500 = (
        874,
        32767,
        88,
        -872,
        -7500,
    )
    VALUE_32767_3398_282_420_32768_450_42 = (
        32767,
        3398,
        282,
        420,
        -32768,
        -450,
        -42,
    )
    VALUE_880_32767_638_15_841_2390_9649_2651_1247 = (
        -880,
        32767,
        -638,
        15,
        -841,
        -2390,
        9649,
        -2651,
        1247,
    )
    VALUE_11452_451_178_399_6131_20057_2229_94_48_32767 = (
        -11452,
        -451,
        -178,
        -399,
        6131,
        -20057,
        2229,
        -94,
        48,
        32767,
    )
    VALUE_254_7010_175_201_107 = (
        254,
        -7010,
        -175,
        -201,
        107,
    )
    VALUE_4879_756_5172_4139_408_20825 = (
        4879,
        -756,
        5172,
        -4139,
        408,
        20825,
    )
    VALUE_32767_868_901_60_5_85_7655_2844_52 = (
        32767,
        -868,
        901,
        60,
        5,
        85,
        7655,
        -2844,
        52,
    )


@dataclass(kw_only=True)
class NistschemaSvIvListShortEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-short-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-short-enumeration-5-NS"

    value: NistschemaSvIvListShortEnumeration5Type = field()
