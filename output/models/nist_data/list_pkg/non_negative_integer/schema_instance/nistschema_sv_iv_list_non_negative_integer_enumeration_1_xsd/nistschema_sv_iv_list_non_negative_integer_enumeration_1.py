from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-nonNegativeInteger-enumeration-1-NS"


class NistschemaSvIvListNonNegativeIntegerEnumeration1Type(Enum):
    VALUE_9_18457155621357_8214449301_556309945930_2355140274_3618563_9596_605822595983 = (
            9,
            18457155621357,
            8214449301,
            556309945930,
            2355140274,
            3618563,
            9596,
            605822595983,
        )
    VALUE_18961_595_6507_82216_980133 = (
            18961,
            595,
            6507,
            82216,
            980133,
        )
    VALUE_688614_58114_9703_1520749026931863_46376_7711_132_979065 = (
            688614,
            58114,
            9703,
            1520749026931863,
            46376,
            7711,
            132,
            979065,
        )
    VALUE_2323_671431443325_8754108031229654_66183_909124488090_98_884694050 = (
            2323,
            671431443325,
            8754108031229654,
            66183,
            909124488090,
            98,
            884694050,
        )
    VALUE_705612658119_58864219_134504815013_72083367913_94946364030 = (
            705612658119,
            58864219,
            134504815013,
            72083367913,
            94946364030,
        )
    VALUE_32544603516952075_13748080127884731_46804_89163_807597789630769_51350 = (
            32544603516952075,
            13748080127884731,
            46804,
            89163,
            807597789630769,
            51350,
        )


@dataclass
class NistschemaSvIvListNonNegativeIntegerEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-nonNegativeInteger-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-nonNegativeInteger-enumeration-1-NS"

    value: Optional[NistschemaSvIvListNonNegativeIntegerEnumeration1Type] = field(
        default=None
    )
