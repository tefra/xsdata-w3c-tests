from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    """
    :ivar value_00:
    :ivar value_01:
    :ivar value_02:
    :ivar value_10:
    :ivar value_11:
    :ivar value_12:
    :ivar value_20:
    :ivar value_30:
    :ivar value_40:
    :ivar value_50:
    :ivar value_60:
    :ivar value_70:
    :ivar value_80:
    :ivar value_81:
    :ivar value_82:
    :ivar value_90:
    """
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    value_00: Optional[int] = field(
        default=None,
        metadata={
            "name": "ᄋ00",
            "type": "Attribute",
        }
    )
    value_01: Optional[int] = field(
        default=None,
        metadata={
            "name": "ᄋ01",
            "type": "Attribute",
        }
    )
    value_02: Optional[int] = field(
        default=None,
        metadata={
            "name": "ᄌ02",
            "type": "Attribute",
        }
    )
    value_10: Optional[int] = field(
        default=None,
        metadata={
            "name": "ᄎ10",
            "type": "Attribute",
        }
    )
    value_11: Optional[int] = field(
        default=None,
        metadata={
            "name": "ᄐ11",
            "type": "Attribute",
        }
    )
    value_12: Optional[int] = field(
        default=None,
        metadata={
            "name": "ᄒ12",
            "type": "Attribute",
        }
    )
    value_20: Optional[int] = field(
        default=None,
        metadata={
            "name": "ᄼ20",
            "type": "Attribute",
        }
    )
    value_30: Optional[int] = field(
        default=None,
        metadata={
            "name": "ᄾ30",
            "type": "Attribute",
        }
    )
    value_40: Optional[int] = field(
        default=None,
        metadata={
            "name": "ᅀ40",
            "type": "Attribute",
        }
    )
    value_50: Optional[int] = field(
        default=None,
        metadata={
            "name": "ᅌ50",
            "type": "Attribute",
        }
    )
    value_60: Optional[int] = field(
        default=None,
        metadata={
            "name": "ᅎ60",
            "type": "Attribute",
        }
    )
    value_70: Optional[int] = field(
        default=None,
        metadata={
            "name": "ᅐ70",
            "type": "Attribute",
        }
    )
    value_80: Optional[int] = field(
        default=None,
        metadata={
            "name": "ᅔ80",
            "type": "Attribute",
        }
    )
    value_81: Optional[int] = field(
        default=None,
        metadata={
            "name": "ᅔ81",
            "type": "Attribute",
        }
    )
    value_82: Optional[int] = field(
        default=None,
        metadata={
            "name": "ᅕ82",
            "type": "Attribute",
        }
    )
    value_90: Optional[int] = field(
        default=None,
        metadata={
            "name": "ᅙ90",
            "type": "Attribute",
        }
    )
