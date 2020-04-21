from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Root:
    """
    :ivar content:
    :ivar e:
    """
    class Meta:
        name = "root"
        nillable = True

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    e: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
