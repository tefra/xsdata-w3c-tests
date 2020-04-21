from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "compositor"


@dataclass
class A:
    """
    :ivar date:
    :ivar time:
    :ivar name:
    """
    class Meta:
        name = "a"
        namespace = "compositor"

    date: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    time: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
