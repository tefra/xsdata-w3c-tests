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
            "name": "ᅟ00",
            "type": "Attribute",
        },
    )
    value_01: None | int = field(
        default=None,
        metadata={
            "name": "ᅠ01",
            "type": "Attribute",
        },
    )
    value_02: None | int = field(
        default=None,
        metadata={
            "name": "ᅡ02",
            "type": "Attribute",
        },
    )
    value_10: None | int = field(
        default=None,
        metadata={
            "name": "ᅣ10",
            "type": "Attribute",
        },
    )
    value_20: None | int = field(
        default=None,
        metadata={
            "name": "ᅥ20",
            "type": "Attribute",
        },
    )
    value_30: None | int = field(
        default=None,
        metadata={
            "name": "ᅧ30",
            "type": "Attribute",
        },
    )
    value_40: None | int = field(
        default=None,
        metadata={
            "name": "ᅩ40",
            "type": "Attribute",
        },
    )
    value_50: None | int = field(
        default=None,
        metadata={
            "name": "ᅭ50",
            "type": "Attribute",
        },
    )
    value_51: None | int = field(
        default=None,
        metadata={
            "name": "ᅭ51",
            "type": "Attribute",
        },
    )
    value_52: None | int = field(
        default=None,
        metadata={
            "name": "ᅮ52",
            "type": "Attribute",
        },
    )
    value_60: None | int = field(
        default=None,
        metadata={
            "name": "ᅲ60",
            "type": "Attribute",
        },
    )
    value_61: None | int = field(
        default=None,
        metadata={
            "name": "ᅲ61",
            "type": "Attribute",
        },
    )
    value_62: None | int = field(
        default=None,
        metadata={
            "name": "ᅳ62",
            "type": "Attribute",
        },
    )
    value_70: None | int = field(
        default=None,
        metadata={
            "name": "ᅵ70",
            "type": "Attribute",
        },
    )
    value_80: None | int = field(
        default=None,
        metadata={
            "name": "ᆞ80",
            "type": "Attribute",
        },
    )
    value_90: None | int = field(
        default=None,
        metadata={
            "name": "ᆨ90",
            "type": "Attribute",
        },
    )
