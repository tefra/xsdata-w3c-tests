from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Ids:
    """
    :ivar id1:
    """
    class Meta:
        name = "ids"

    id1: str = field(
        default="zxc",
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root:
    """
    :ivar a:
    """
    class Meta:
        name = "root"

    a: Optional[Ids] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
