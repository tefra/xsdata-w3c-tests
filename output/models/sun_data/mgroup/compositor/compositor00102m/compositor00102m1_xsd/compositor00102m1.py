from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "compositor"


@dataclass
class A:
    """
    :ivar date:
    :ivar time:
    """
    class Meta:
        name = "a"
        namespace = "compositor"

    date: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    time: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )