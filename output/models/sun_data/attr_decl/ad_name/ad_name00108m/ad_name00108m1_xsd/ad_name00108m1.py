from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    str00_aa: Optional[str] = field(
        default=None,
        metadata={
            "name": "str00AA",
            "type": "Attribute",
        },
    )
    str10_m: Optional[str] = field(
        default=None,
        metadata={
            "name": "str10-M",
            "type": "Attribute",
        },
    )
    str20_z: Optional[str] = field(
        default=None,
        metadata={
            "name": "str20Z",
            "type": "Attribute",
        },
    )
    str01_aa: Optional[str] = field(
        default=None,
        metadata={
            "name": "str01Aa",
            "type": "Attribute",
        },
    )
    str11_d: Optional[str] = field(
        default=None,
        metadata={
            "name": "str11-d",
            "type": "Attribute",
        },
    )
    str21h: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    str02_aj: Optional[str] = field(
        default=None,
        metadata={
            "name": "str02Aj",
            "type": "Attribute",
        },
    )
    str12_r: Optional[str] = field(
        default=None,
        metadata={
            "name": "str12-r",
            "type": "Attribute",
        },
    )
    str22z: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    str03_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str03AÀ",
            "type": "Attribute",
        },
    )
    str13: Optional[str] = field(
        default=None,
        metadata={
            "name": "str13-Ë",
            "type": "Attribute",
        },
    )
    str23: Optional[str] = field(
        default=None,
        metadata={
            "name": "str23Ö",
            "type": "Attribute",
        },
    )
    str04_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str04AØ",
            "type": "Attribute",
        },
    )
    str14: Optional[str] = field(
        default=None,
        metadata={
            "name": "str14-Û",
            "type": "Attribute",
        },
    )
    str24: Optional[str] = field(
        default=None,
        metadata={
            "name": "str24Þ",
            "type": "Attribute",
        },
    )
    str05_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str05Aà",
            "type": "Attribute",
        },
    )
    str15: Optional[str] = field(
        default=None,
        metadata={
            "name": "str15-ë",
            "type": "Attribute",
        },
    )
    str25: Optional[str] = field(
        default=None,
        metadata={
            "name": "str25ö",
            "type": "Attribute",
        },
    )
    str06_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str06Aø",
            "type": "Attribute",
        },
    )
    str16: Optional[str] = field(
        default=None,
        metadata={
            "name": "str16-û",
            "type": "Attribute",
        },
    )
    str26: Optional[str] = field(
        default=None,
        metadata={
            "name": "str26ÿ",
            "type": "Attribute",
        },
    )
    str07_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str07AĀ",
            "type": "Attribute",
        },
    )
    str17: Optional[str] = field(
        default=None,
        metadata={
            "name": "str17-Ę",
            "type": "Attribute",
        },
    )
    str27: Optional[str] = field(
        default=None,
        metadata={
            "name": "str27ı",
            "type": "Attribute",
        },
    )
    str08_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str08AĴ",
            "type": "Attribute",
        },
    )
    str18: Optional[str] = field(
        default=None,
        metadata={
            "name": "str18-Ĺ",
            "type": "Attribute",
        },
    )
    str28: Optional[str] = field(
        default=None,
        metadata={
            "name": "str28ľ",
            "type": "Attribute",
        },
    )
    str09_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str09AŁ",
            "type": "Attribute",
        },
    )
    str19: Optional[str] = field(
        default=None,
        metadata={
            "name": "str19-ń",
            "type": "Attribute",
        },
    )
    str29: Optional[str] = field(
        default=None,
        metadata={
            "name": "str29ň",
            "type": "Attribute",
        },
    )
