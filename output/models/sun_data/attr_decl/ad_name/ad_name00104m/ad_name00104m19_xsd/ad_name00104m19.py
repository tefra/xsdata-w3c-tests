from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    value_00: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ạ00",
            "type": "Attribute",
        }
    )
    value_01: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ọ01",
            "type": "Attribute",
        }
    )
    value_02: Optional[int] = field(
        default=None,
        metadata={
            "name": "ỹ02",
            "type": "Attribute",
        }
    )
    value_10: Optional[int] = field(
        default=None,
        metadata={
            "name": "ἀ10",
            "type": "Attribute",
        }
    )
    value_11: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ἂ11",
            "type": "Attribute",
        }
    )
    value_12: Optional[int] = field(
        default=None,
        metadata={
            "name": "ἕ12",
            "type": "Attribute",
        }
    )
    value_20: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ἐ20",
            "type": "Attribute",
        }
    )
    value_21: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ἒ21",
            "type": "Attribute",
        }
    )
    value_22: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ἕ22",
            "type": "Attribute",
        }
    )
    value_30: Optional[int] = field(
        default=None,
        metadata={
            "name": "ἠ30",
            "type": "Attribute",
        }
    )
    value_31: Optional[int] = field(
        default=None,
        metadata={
            "name": "ἲ31",
            "type": "Attribute",
        }
    )
    value_32: Optional[int] = field(
        default=None,
        metadata={
            "name": "ὅ32",
            "type": "Attribute",
        }
    )
    value_40: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ὀ40",
            "type": "Attribute",
        }
    )
    value_41: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ὂ41",
            "type": "Attribute",
        }
    )
    value_42: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ὅ42",
            "type": "Attribute",
        }
    )
    value_50: Optional[int] = field(
        default=None,
        metadata={
            "name": "ὑ50",
            "type": "Attribute",
        }
    )
    value_60: Optional[int] = field(
        default=None,
        metadata={
            "name": "ὓ60",
            "type": "Attribute",
        }
    )
    value_70: Optional[int] = field(
        default=None,
        metadata={
            "name": "ὕ70",
            "type": "Attribute",
        }
    )
    value_80: Optional[int] = field(
        default=None,
        metadata={
            "name": "ὗ80",
            "type": "Attribute",
        }
    )
    value_90: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ὑ90",
            "type": "Attribute",
        }
    )
