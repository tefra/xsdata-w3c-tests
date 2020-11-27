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
            "name": "str00Aᅟ",
            "type": "Attribute",
        }
    )
    str10: Optional[str] = field(
        default=None,
        metadata={
            "name": "str10-ᅠ",
            "type": "Attribute",
        }
    )
    str20: Optional[str] = field(
        default=None,
        metadata={
            "name": "str20ᅡ",
            "type": "Attribute",
        }
    )
    str01_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str01Aᅣ",
            "type": "Attribute",
        }
    )
    str02_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str02Aᅥ",
            "type": "Attribute",
        }
    )
    str03_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str03Aᅧ",
            "type": "Attribute",
        }
    )
    str04_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str04Aᅩ",
            "type": "Attribute",
        }
    )
    str05_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str05Aᅭ",
            "type": "Attribute",
        }
    )
    str15: Optional[str] = field(
        default=None,
        metadata={
            "name": "str15-ᅭ",
            "type": "Attribute",
        }
    )
    str25: Optional[str] = field(
        default=None,
        metadata={
            "name": "str25ᅮ",
            "type": "Attribute",
        }
    )
    str06_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str06Aᅲ",
            "type": "Attribute",
        }
    )
    str16: Optional[str] = field(
        default=None,
        metadata={
            "name": "str16-ᅲ",
            "type": "Attribute",
        }
    )
    str26: Optional[str] = field(
        default=None,
        metadata={
            "name": "str26ᅳ",
            "type": "Attribute",
        }
    )
    str07_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str07Aᅵ",
            "type": "Attribute",
        }
    )
    str08_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str08Aᆞ",
            "type": "Attribute",
        }
    )
    str09_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str09Aᆨ",
            "type": "Attribute",
        }
    )
