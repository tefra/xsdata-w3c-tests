from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-byte-enumeration-1-NS"


class NistschemaSvIvListByteEnumeration1Type(Enum):
    VALUE_50_128_70_66_99_37_31_6 = (
            50,
            -128,
            70,
            66,
            -99,
            -37,
            31,
            -6,
        )
    VALUE_128_127_6_4_98_52_45_114 = (
            -128,
            127,
            -6,
            -4,
            -98,
            52,
            -45,
            -114,
        )
    VALUE_127_49_86_6_64_7_76_128_34 = (
            127,
            49,
            86,
            -6,
            -64,
            -7,
            76,
            -128,
            -34,
        )
    VALUE_127_43_15_126_14_63_128_94 = (
            127,
            -43,
            -15,
            -126,
            -14,
            -63,
            -128,
            94,
        )
    VALUE_126_77_53_8_4_127_74_128_2 = (
            126,
            -77,
            -53,
            8,
            -4,
            127,
            -74,
            -128,
            -2,
        )
    VALUE_38_6_9_80_128_127_68 = (
            -38,
            -6,
            9,
            -80,
            -128,
            127,
            -68,
        )
    VALUE_89_40_2_59_6_128_70_19_9 = (
            -89,
            40,
            -2,
            -59,
            6,
            -128,
            -70,
            19,
            -9,
        )
    VALUE_128_74_95_27_86_63_127_75 = (
            -128,
            74,
            -95,
            27,
            -86,
            63,
            127,
            75,
        )


@dataclass
class NistschemaSvIvListByteEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-byte-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-byte-enumeration-1-NS"

    value: Optional[NistschemaSvIvListByteEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
