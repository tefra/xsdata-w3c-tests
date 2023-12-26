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
            "name": "str00A·",
            "type": "Attribute",
        },
    )
    str01_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str01Aː",
            "type": "Attribute",
        },
    )
    str02_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str02Aˑ",
            "type": "Attribute",
        },
    )
    str03_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str03A·",
            "type": "Attribute",
        },
    )
    str04_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str04Aـ",
            "type": "Attribute",
        },
    )
    str05_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str05Aๆ",
            "type": "Attribute",
        },
    )
    str06_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str06Aໆ",
            "type": "Attribute",
        },
    )
    str07_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str07A々",
            "type": "Attribute",
        },
    )
    str08_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str08A〱",
            "type": "Attribute",
        },
    )
    str18: Optional[str] = field(
        default=None,
        metadata={
            "name": "str18-〳",
            "type": "Attribute",
        },
    )
    str28: Optional[str] = field(
        default=None,
        metadata={
            "name": "str28〵",
            "type": "Attribute",
        },
    )
    str09_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str09Aゝ",
            "type": "Attribute",
        },
    )
    str19: Optional[str] = field(
        default=None,
        metadata={
            "name": "str19-ゝ",
            "type": "Attribute",
        },
    )
    str29: Optional[str] = field(
        default=None,
        metadata={
            "name": "str29ゞ",
            "type": "Attribute",
        },
    )
