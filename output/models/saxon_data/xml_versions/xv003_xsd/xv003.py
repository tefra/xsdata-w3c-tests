from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    """
    :ivar content:
    :ivar att:
    """
    class Meta:
        name = "doc"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    att: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
