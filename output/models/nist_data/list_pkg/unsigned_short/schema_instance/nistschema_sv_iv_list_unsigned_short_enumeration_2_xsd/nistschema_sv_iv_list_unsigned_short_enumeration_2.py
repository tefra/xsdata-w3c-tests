from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedShort-enumeration-2-NS"


class NistschemaSvIvListUnsignedShortEnumeration2Type(Enum):
    VALUE_65535_856_50539_26_665_7_533_3203 = (
        65535,
        856,
        50539,
        26,
        665,
        7,
        533,
        3203,
    )
    VALUE_117_7076_46_40_727_1343_3889_5_847 = (
        117,
        7076,
        46,
        40,
        727,
        1343,
        3889,
        5,
        847,
    )
    VALUE_873_80_920_65535_47966_968_82_5243_220 = (
        873,
        80,
        920,
        65535,
        47966,
        968,
        82,
        5243,
        220,
    )
    VALUE_6808_196_53_65535_362_63_9222 = (
        6808,
        196,
        53,
        65535,
        362,
        63,
        9222,
    )
    VALUE_54_6745_28655_995_65535_907_106_713 = (
        54,
        6745,
        28655,
        995,
        65535,
        907,
        106,
        713,
    )
    VALUE_3097_84_60_299_40_10_67 = (
        3097,
        84,
        60,
        299,
        40,
        10,
        67,
    )


@dataclass(kw_only=True)
class NistschemaSvIvListUnsignedShortEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedShort-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-unsignedShort-enumeration-2-NS"

    value: NistschemaSvIvListUnsignedShortEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
