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
    :ivar value_20:
    :ivar value_30:
    :ivar value_40:
    :ivar value_50:
    :ivar value_51:
    :ivar value_52:
    :ivar value_60:
    :ivar value_61:
    :ivar value_62:
    :ivar value_70:
    :ivar value_80:
    :ivar value_90:
    """
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    value_00: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ᅟ00",
            type="Attribute"
        )
    )
    value_01: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ᅠ01",
            type="Attribute"
        )
    )
    value_02: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ᅡ02",
            type="Attribute"
        )
    )
    value_10: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ᅣ10",
            type="Attribute"
        )
    )
    value_20: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ᅥ20",
            type="Attribute"
        )
    )
    value_30: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ᅧ30",
            type="Attribute"
        )
    )
    value_40: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ᅩ40",
            type="Attribute"
        )
    )
    value_50: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ᅭ50",
            type="Attribute"
        )
    )
    value_51: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ᅭ51",
            type="Attribute"
        )
    )
    value_52: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ᅮ52",
            type="Attribute"
        )
    )
    value_60: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ᅲ60",
            type="Attribute"
        )
    )
    value_61: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ᅲ61",
            type="Attribute"
        )
    )
    value_62: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ᅳ62",
            type="Attribute"
        )
    )
    value_70: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ᅵ70",
            type="Attribute"
        )
    )
    value_80: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ᆞ80",
            type="Attribute"
        )
    )
    value_90: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ᆨ90",
            type="Attribute"
        )
    )
