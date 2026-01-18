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
            "name": "str00Aᅟ",
            "type": "Attribute",
        },
    )
    str10: None | str = field(
        default=None,
        metadata={
            "name": "str10-ᅠ",
            "type": "Attribute",
        },
    )
    str20: None | str = field(
        default=None,
        metadata={
            "name": "str20ᅡ",
            "type": "Attribute",
        },
    )
    str01_a: None | str = field(
        default=None,
        metadata={
            "name": "str01Aᅣ",
            "type": "Attribute",
        },
    )
    str02_a: None | str = field(
        default=None,
        metadata={
            "name": "str02Aᅥ",
            "type": "Attribute",
        },
    )
    str03_a: None | str = field(
        default=None,
        metadata={
            "name": "str03Aᅧ",
            "type": "Attribute",
        },
    )
    str04_a: None | str = field(
        default=None,
        metadata={
            "name": "str04Aᅩ",
            "type": "Attribute",
        },
    )
    str05_a: None | str = field(
        default=None,
        metadata={
            "name": "str05Aᅭ",
            "type": "Attribute",
        },
    )
    str15: None | str = field(
        default=None,
        metadata={
            "name": "str15-ᅭ",
            "type": "Attribute",
        },
    )
    str25: None | str = field(
        default=None,
        metadata={
            "name": "str25ᅮ",
            "type": "Attribute",
        },
    )
    str06_a: None | str = field(
        default=None,
        metadata={
            "name": "str06Aᅲ",
            "type": "Attribute",
        },
    )
    str16: None | str = field(
        default=None,
        metadata={
            "name": "str16-ᅲ",
            "type": "Attribute",
        },
    )
    str26: None | str = field(
        default=None,
        metadata={
            "name": "str26ᅳ",
            "type": "Attribute",
        },
    )
    str07_a: None | str = field(
        default=None,
        metadata={
            "name": "str07Aᅵ",
            "type": "Attribute",
        },
    )
    str08_a: None | str = field(
        default=None,
        metadata={
            "name": "str08Aᆞ",
            "type": "Attribute",
        },
    )
    str09_a: None | str = field(
        default=None,
        metadata={
            "name": "str09Aᆨ",
            "type": "Attribute",
        },
    )
