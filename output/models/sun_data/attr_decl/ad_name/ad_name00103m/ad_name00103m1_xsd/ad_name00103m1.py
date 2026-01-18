from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "AttrDecl/name"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    str00_a: None | str = field(
        default=None,
        metadata={
            "name": "str00A·",
            "type": "Attribute",
        },
    )
    str01_a: None | str = field(
        default=None,
        metadata={
            "name": "str01Aː",
            "type": "Attribute",
        },
    )
    str02_a: None | str = field(
        default=None,
        metadata={
            "name": "str02Aˑ",
            "type": "Attribute",
        },
    )
    str03_a: None | str = field(
        default=None,
        metadata={
            "name": "str03A·",
            "type": "Attribute",
        },
    )
    str04_a: None | str = field(
        default=None,
        metadata={
            "name": "str04Aـ",
            "type": "Attribute",
        },
    )
    str05_a: None | str = field(
        default=None,
        metadata={
            "name": "str05Aๆ",
            "type": "Attribute",
        },
    )
    str06_a: None | str = field(
        default=None,
        metadata={
            "name": "str06Aໆ",
            "type": "Attribute",
        },
    )
    str07_a: None | str = field(
        default=None,
        metadata={
            "name": "str07A々",
            "type": "Attribute",
        },
    )
    str08_a: None | str = field(
        default=None,
        metadata={
            "name": "str08A〱",
            "type": "Attribute",
        },
    )
    str18: None | str = field(
        default=None,
        metadata={
            "name": "str18-〳",
            "type": "Attribute",
        },
    )
    str28: None | str = field(
        default=None,
        metadata={
            "name": "str28〵",
            "type": "Attribute",
        },
    )
    str09_a: None | str = field(
        default=None,
        metadata={
            "name": "str09Aゝ",
            "type": "Attribute",
        },
    )
    str19: None | str = field(
        default=None,
        metadata={
            "name": "str19-ゝ",
            "type": "Attribute",
        },
    )
    str29: None | str = field(
        default=None,
        metadata={
            "name": "str29ゞ",
            "type": "Attribute",
        },
    )
