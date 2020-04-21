from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://example.com/over019"


@dataclass
class Para:
    """
    :ivar value:
    """
    class Meta:
        name = "para"
        namespace = "http://example.com/over019"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
