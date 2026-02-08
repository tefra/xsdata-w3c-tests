from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedByte-enumeration-4-NS"


class NistschemaSvIvListUnsignedByteEnumeration4Type(Enum):
    VALUE_68_9_255_17_84_28 = (
        68,
        9,
        255,
        17,
        84,
        28,
    )
    VALUE_32_255_19_33_7_10_36_37_11 = (
        32,
        255,
        19,
        33,
        7,
        10,
        36,
        37,
        11,
    )
    VALUE_3_9_31_56_81_11_255_10_92 = (
        3,
        9,
        31,
        56,
        81,
        11,
        255,
        10,
        92,
    )
    VALUE_255_57_86_3_48_17 = (
        255,
        57,
        86,
        3,
        48,
        17,
    )
    VALUE_85_255_41_33_28_44 = (
        85,
        255,
        41,
        33,
        28,
        44,
    )
    VALUE_47_255_91_217_8_90_11 = (
        47,
        255,
        91,
        217,
        8,
        90,
        11,
    )


@dataclass(kw_only=True)
class NistschemaSvIvListUnsignedByteEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedByte-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-unsignedByte-enumeration-4-NS"

    value: NistschemaSvIvListUnsignedByteEnumeration4Type = field()
