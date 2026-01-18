from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "AttrDecl/name"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    a00: None | int = field(
        default=None,
        metadata={
            "name": "A00",
            "type": "Attribute",
        },
    )
    m01: None | int = field(
        default=None,
        metadata={
            "name": "M01",
            "type": "Attribute",
        },
    )
    z02: None | int = field(
        default=None,
        metadata={
            "name": "Z02",
            "type": "Attribute",
        },
    )
    a10: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    d11: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    h12: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    j20: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    r21: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    z22: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value_30: None | int = field(
        default=None,
        metadata={
            "name": "À30",
            "type": "Attribute",
        },
    )
    value_31: None | int = field(
        default=None,
        metadata={
            "name": "Ë31",
            "type": "Attribute",
        },
    )
    value_32: None | int = field(
        default=None,
        metadata={
            "name": "Ö32",
            "type": "Attribute",
        },
    )
    value_40: None | int = field(
        default=None,
        metadata={
            "name": "Ø40",
            "type": "Attribute",
        },
    )
    value_41: None | int = field(
        default=None,
        metadata={
            "name": "Û41",
            "type": "Attribute",
        },
    )
    value_42: None | int = field(
        default=None,
        metadata={
            "name": "Þ42",
            "type": "Attribute",
        },
    )
    value_50: None | int = field(
        default=None,
        metadata={
            "name": "à50",
            "type": "Attribute",
        },
    )
    value_51: None | int = field(
        default=None,
        metadata={
            "name": "ë51",
            "type": "Attribute",
        },
    )
    value_52: None | int = field(
        default=None,
        metadata={
            "name": "ö52",
            "type": "Attribute",
        },
    )
    value_60: None | int = field(
        default=None,
        metadata={
            "name": "ø60",
            "type": "Attribute",
        },
    )
    value_61: None | int = field(
        default=None,
        metadata={
            "name": "û61",
            "type": "Attribute",
        },
    )
    value_62: None | int = field(
        default=None,
        metadata={
            "name": "ÿ62",
            "type": "Attribute",
        },
    )
    value_70: None | int = field(
        default=None,
        metadata={
            "name": "Ā70",
            "type": "Attribute",
        },
    )
    value_71: None | int = field(
        default=None,
        metadata={
            "name": "Ę71",
            "type": "Attribute",
        },
    )
    value_72: None | int = field(
        default=None,
        metadata={
            "name": "ı72",
            "type": "Attribute",
        },
    )
    value_80: None | int = field(
        default=None,
        metadata={
            "name": "Ĵ80",
            "type": "Attribute",
        },
    )
    value_81: None | int = field(
        default=None,
        metadata={
            "name": "Ĺ81",
            "type": "Attribute",
        },
    )
    value_82: None | int = field(
        default=None,
        metadata={
            "name": "ľ82",
            "type": "Attribute",
        },
    )
    value_90: None | int = field(
        default=None,
        metadata={
            "name": "Ł90",
            "type": "Attribute",
        },
    )
    value_91: None | int = field(
        default=None,
        metadata={
            "name": "ń91",
            "type": "Attribute",
        },
    )
    value_92: None | int = field(
        default=None,
        metadata={
            "name": "ň92",
            "type": "Attribute",
        },
    )
