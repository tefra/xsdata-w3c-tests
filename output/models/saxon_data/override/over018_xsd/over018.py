from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://example.com/over018"


@dataclass
class Doc:
    """
    :ivar value:
    """
    class Meta:
        name = "doc"
        namespace = "http://example.com/over018"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
