from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    """
    :ivar att:
    """
    class Meta:
        name = "doc"

    att: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
