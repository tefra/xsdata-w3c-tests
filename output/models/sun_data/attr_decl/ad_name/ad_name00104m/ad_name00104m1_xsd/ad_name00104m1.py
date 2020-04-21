from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    """
    :ivar a00:
    :ivar m01:
    :ivar z02:
    :ivar a10:
    :ivar d11:
    :ivar h12:
    :ivar j20:
    :ivar r21:
    :ivar z22:
    :ivar value_30:
    :ivar value_31:
    :ivar value_32:
    :ivar value_40:
    :ivar value_41:
    :ivar value_42:
    :ivar value_50:
    :ivar value_51:
    :ivar value_52:
    :ivar value_60:
    :ivar value_61:
    :ivar value_62:
    :ivar value_70:
    :ivar value_71:
    :ivar value_72:
    :ivar value_80:
    :ivar value_81:
    :ivar value_82:
    :ivar value_90:
    :ivar value_91:
    :ivar value_92:
    """
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    a00: Optional[int] = field(
        default=None,
        metadata=dict(
            name="A00",
            type="Attribute"
        )
    )
    m01: Optional[int] = field(
        default=None,
        metadata=dict(
            name="M01",
            type="Attribute"
        )
    )
    z02: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Z02",
            type="Attribute"
        )
    )
    a10: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    d11: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    h12: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    j20: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    r21: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    z22: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    value_30: Optional[int] = field(
        default=None,
        metadata=dict(
            name="À30",
            type="Attribute"
        )
    )
    value_31: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Ë31",
            type="Attribute"
        )
    )
    value_32: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Ö32",
            type="Attribute"
        )
    )
    value_40: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Ø40",
            type="Attribute"
        )
    )
    value_41: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Û41",
            type="Attribute"
        )
    )
    value_42: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Þ42",
            type="Attribute"
        )
    )
    value_50: Optional[int] = field(
        default=None,
        metadata=dict(
            name="à50",
            type="Attribute"
        )
    )
    value_51: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ë51",
            type="Attribute"
        )
    )
    value_52: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ö52",
            type="Attribute"
        )
    )
    value_60: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ø60",
            type="Attribute"
        )
    )
    value_61: Optional[int] = field(
        default=None,
        metadata=dict(
            name="û61",
            type="Attribute"
        )
    )
    value_62: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ÿ62",
            type="Attribute"
        )
    )
    value_70: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Ā70",
            type="Attribute"
        )
    )
    value_71: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Ę71",
            type="Attribute"
        )
    )
    value_72: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ı72",
            type="Attribute"
        )
    )
    value_80: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Ĵ80",
            type="Attribute"
        )
    )
    value_81: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Ĺ81",
            type="Attribute"
        )
    )
    value_82: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ľ82",
            type="Attribute"
        )
    )
    value_90: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Ł90",
            type="Attribute"
        )
    )
    value_91: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ń91",
            type="Attribute"
        )
    )
    value_92: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ň92",
            type="Attribute"
        )
    )
