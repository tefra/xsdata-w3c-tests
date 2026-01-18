from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "AttrDecl/name"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    value_00: None | int = field(
        default=None,
        metadata={
            "name": "Ạ00",
            "type": "Attribute",
        },
    )
    value_01: None | int = field(
        default=None,
        metadata={
            "name": "Ọ01",
            "type": "Attribute",
        },
    )
    value_02: None | int = field(
        default=None,
        metadata={
            "name": "ỹ02",
            "type": "Attribute",
        },
    )
    value_10: None | int = field(
        default=None,
        metadata={
            "name": "ἀ10",
            "type": "Attribute",
        },
    )
    value_11: None | int = field(
        default=None,
        metadata={
            "name": "Ἂ11",
            "type": "Attribute",
        },
    )
    value_12: None | int = field(
        default=None,
        metadata={
            "name": "ἕ12",
            "type": "Attribute",
        },
    )
    value_20: None | int = field(
        default=None,
        metadata={
            "name": "Ἐ20",
            "type": "Attribute",
        },
    )
    value_21: None | int = field(
        default=None,
        metadata={
            "name": "Ἒ21",
            "type": "Attribute",
        },
    )
    value_22: None | int = field(
        default=None,
        metadata={
            "name": "Ἕ22",
            "type": "Attribute",
        },
    )
    value_30: None | int = field(
        default=None,
        metadata={
            "name": "ἠ30",
            "type": "Attribute",
        },
    )
    value_31: None | int = field(
        default=None,
        metadata={
            "name": "ἲ31",
            "type": "Attribute",
        },
    )
    value_32: None | int = field(
        default=None,
        metadata={
            "name": "ὅ32",
            "type": "Attribute",
        },
    )
    value_40: None | int = field(
        default=None,
        metadata={
            "name": "Ὀ40",
            "type": "Attribute",
        },
    )
    value_41: None | int = field(
        default=None,
        metadata={
            "name": "Ὂ41",
            "type": "Attribute",
        },
    )
    value_42: None | int = field(
        default=None,
        metadata={
            "name": "Ὅ42",
            "type": "Attribute",
        },
    )
    value_50: None | int = field(
        default=None,
        metadata={
            "name": "ὑ50",
            "type": "Attribute",
        },
    )
    value_60: None | int = field(
        default=None,
        metadata={
            "name": "ὓ60",
            "type": "Attribute",
        },
    )
    value_70: None | int = field(
        default=None,
        metadata={
            "name": "ὕ70",
            "type": "Attribute",
        },
    )
    value_80: None | int = field(
        default=None,
        metadata={
            "name": "ὗ80",
            "type": "Attribute",
        },
    )
    value_90: None | int = field(
        default=None,
        metadata={
            "name": "Ὑ90",
            "type": "Attribute",
        },
    )
