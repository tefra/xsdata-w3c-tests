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
    :ivar value_21:
    :ivar value_22:
    """
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    value_00: Optional[int] = field(
        default=None,
        metadata=dict(
            name="一00",
            type="Attribute"
        )
    )
    value_01: Optional[int] = field(
        default=None,
        metadata=dict(
            name="盒01",
            type="Attribute"
        )
    )
    value_02: Optional[int] = field(
        default=None,
        metadata=dict(
            name="龥02",
            type="Attribute"
        )
    )
    value_10: Optional[int] = field(
        default=None,
        metadata=dict(
            name="〇10",
            type="Attribute"
        )
    )
    value_20: Optional[int] = field(
        default=None,
        metadata=dict(
            name="〡20",
            type="Attribute"
        )
    )
    value_21: Optional[int] = field(
        default=None,
        metadata=dict(
            name="〥21",
            type="Attribute"
        )
    )
    value_22: Optional[int] = field(
        default=None,
        metadata=dict(
            name="〩22",
            type="Attribute"
        )
    )
