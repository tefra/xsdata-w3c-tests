from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedShort-enumeration-3-NS"


class NistschemaSvIvListUnsignedShortEnumeration3Type(Enum):
    VALUE_9380_745_96_8282_29_404_5192_60973_533 = (
        9380,
        745,
        96,
        8282,
        29,
        404,
        5192,
        60973,
        533,
    )
    VALUE_188_957_28_65535_72_45_31910_13 = (
        188,
        957,
        28,
        65535,
        72,
        45,
        31910,
        13,
    )
    VALUE_772_2581_9_24_7436 = (
        772,
        2581,
        9,
        24,
        7436,
    )
    VALUE_1_5_21431_2135_45_7554_74 = (
        1,
        5,
        21431,
        2135,
        45,
        7554,
        74,
    )
    VALUE_19_281_85_469_961_2800 = (
        19,
        281,
        85,
        469,
        961,
        2800,
    )
    VALUE_14_45_380_1507_65535 = (
        14,
        45,
        380,
        1507,
        65535,
    )
    VALUE_31_744_80_65535_133_2_40542_6520_92_287 = (
        31,
        744,
        80,
        65535,
        133,
        2,
        40542,
        6520,
        92,
        287,
    )


@dataclass
class NistschemaSvIvListUnsignedShortEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedShort-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-unsignedShort-enumeration-3-NS"

    value: Optional[NistschemaSvIvListUnsignedShortEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
