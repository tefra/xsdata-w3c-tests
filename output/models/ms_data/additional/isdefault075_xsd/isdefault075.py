from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Root:
    """
    :ivar content:
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "root"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    e1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    e2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
