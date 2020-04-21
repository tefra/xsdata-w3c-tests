from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://example.com/over018"


@dataclass
class Para:
    """
    :ivar value:
    """
    class Meta:
        name = "para"
        namespace = "http://example.com/over018"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
