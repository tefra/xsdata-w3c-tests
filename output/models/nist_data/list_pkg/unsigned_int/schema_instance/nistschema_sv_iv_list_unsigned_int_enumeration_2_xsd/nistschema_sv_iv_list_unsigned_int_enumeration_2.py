from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedInt-enumeration-2-NS"


class NistschemaSvIvListUnsignedIntEnumeration2Type(Enum):
    VALUE_48415_91_1576697_37028341_414514_749_25_444_74104_306816661 = (
        48415,
        91,
        1576697,
        37028341,
        414514,
        749,
        25,
        444,
        74104,
        306816661,
    )
    VALUE_33937768_42_1904156_4294967295_4513 = (
        33937768,
        42,
        1904156,
        4294967295,
        4513,
    )
    VALUE_51_6683623_951_1860_7522277_4756_54446757_7687934_4911011 = (
        51,
        6683623,
        951,
        1860,
        7522277,
        4756,
        54446757,
        7687934,
        4911011,
    )
    VALUE_65492818_31_4982461_41_216498879_95361776_6008522_74598_472403602_1054 = (
        65492818,
        31,
        4982461,
        41,
        216498879,
        95361776,
        6008522,
        74598,
        472403602,
        1054,
    )
    VALUE_687_85_231295872_3048_9794_50_628_55779 = (
        687,
        85,
        231295872,
        3048,
        9794,
        50,
        628,
        55779,
    )
    VALUE_240_255035_443551_55547749_724868016_8091766_29171_9250 = (
        240,
        255035,
        443551,
        55547749,
        724868016,
        8091766,
        29171,
        9250,
    )
    VALUE_29497859_4294967295_6306862_12_6016_879267 = (
        29497859,
        4294967295,
        6306862,
        12,
        6016,
        879267,
    )


@dataclass(kw_only=True)
class NistschemaSvIvListUnsignedIntEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedInt-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-unsignedInt-enumeration-2-NS"

    value: NistschemaSvIvListUnsignedIntEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
