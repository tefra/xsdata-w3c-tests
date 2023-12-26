from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    a00: Optional[int] = field(
        default=None,
        metadata={
            "name": "A00",
            "type": "Attribute",
        },
    )
    m01: Optional[int] = field(
        default=None,
        metadata={
            "name": "M01",
            "type": "Attribute",
        },
    )
    z02: Optional[int] = field(
        default=None,
        metadata={
            "name": "Z02",
            "type": "Attribute",
        },
    )
    a10: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    d11: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    h12: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    j20: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    r21: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    z22: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value_30: Optional[int] = field(
        default=None,
        metadata={
            "name": "À30",
            "type": "Attribute",
        },
    )
    value_31: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ë31",
            "type": "Attribute",
        },
    )
    value_32: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ö32",
            "type": "Attribute",
        },
    )
    value_40: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ø40",
            "type": "Attribute",
        },
    )
    value_41: Optional[int] = field(
        default=None,
        metadata={
            "name": "Û41",
            "type": "Attribute",
        },
    )
    value_42: Optional[int] = field(
        default=None,
        metadata={
            "name": "Þ42",
            "type": "Attribute",
        },
    )
    value_50: Optional[int] = field(
        default=None,
        metadata={
            "name": "à50",
            "type": "Attribute",
        },
    )
    value_51: Optional[int] = field(
        default=None,
        metadata={
            "name": "ë51",
            "type": "Attribute",
        },
    )
    value_52: Optional[int] = field(
        default=None,
        metadata={
            "name": "ö52",
            "type": "Attribute",
        },
    )
    value_60: Optional[int] = field(
        default=None,
        metadata={
            "name": "ø60",
            "type": "Attribute",
        },
    )
    value_61: Optional[int] = field(
        default=None,
        metadata={
            "name": "û61",
            "type": "Attribute",
        },
    )
    value_62: Optional[int] = field(
        default=None,
        metadata={
            "name": "ÿ62",
            "type": "Attribute",
        },
    )
    value_70: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ā70",
            "type": "Attribute",
        },
    )
    value_71: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ę71",
            "type": "Attribute",
        },
    )
    value_72: Optional[int] = field(
        default=None,
        metadata={
            "name": "ı72",
            "type": "Attribute",
        },
    )
    value_80: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ĵ80",
            "type": "Attribute",
        },
    )
    value_81: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ĺ81",
            "type": "Attribute",
        },
    )
    value_82: Optional[int] = field(
        default=None,
        metadata={
            "name": "ľ82",
            "type": "Attribute",
        },
    )
    value_90: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ł90",
            "type": "Attribute",
        },
    )
    value_91: Optional[int] = field(
        default=None,
        metadata={
            "name": "ń91",
            "type": "Attribute",
        },
    )
    value_92: Optional[int] = field(
        default=None,
        metadata={
            "name": "ň92",
            "type": "Attribute",
        },
    )
