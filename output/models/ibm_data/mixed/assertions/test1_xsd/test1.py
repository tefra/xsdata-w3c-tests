from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Xtype:
    """
    :ivar message:
    :ivar min:
    :ivar max:
    """
    class Meta:
        name = "XType"

    message: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    min: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    max: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class X(Xtype):
    pass
