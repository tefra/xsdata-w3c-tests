from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    str00_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str00Aᄋ",
            "type": "Attribute",
        },
    )
    str10: Optional[str] = field(
        default=None,
        metadata={
            "name": "str10-ᄋ",
            "type": "Attribute",
        },
    )
    str20: Optional[str] = field(
        default=None,
        metadata={
            "name": "str20ᄌ",
            "type": "Attribute",
        },
    )
    str01_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str01Aᄎ",
            "type": "Attribute",
        },
    )
    str11: Optional[str] = field(
        default=None,
        metadata={
            "name": "str11-ᄐ",
            "type": "Attribute",
        },
    )
    str21: Optional[str] = field(
        default=None,
        metadata={
            "name": "str21ᄒ",
            "type": "Attribute",
        },
    )
    str02_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str02Aᄼ",
            "type": "Attribute",
        },
    )
    str03_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str03Aᄾ",
            "type": "Attribute",
        },
    )
    str04_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str04Aᅀ",
            "type": "Attribute",
        },
    )
    str05_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str05Aᅌ",
            "type": "Attribute",
        },
    )
    str06_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str06Aᅎ",
            "type": "Attribute",
        },
    )
    str07_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str07Aᅐ",
            "type": "Attribute",
        },
    )
    str08_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str08Aᅔ",
            "type": "Attribute",
        },
    )
    str18: Optional[str] = field(
        default=None,
        metadata={
            "name": "str18-ᅔ",
            "type": "Attribute",
        },
    )
    str28: Optional[str] = field(
        default=None,
        metadata={
            "name": "str28ᅕ",
            "type": "Attribute",
        },
    )
    str09_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str09Aᅙ",
            "type": "Attribute",
        },
    )
