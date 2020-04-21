from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Title:
    """
    :ivar value:
    """
    class Meta:
        name = "title"
        namespace = "http://www.w3.org/2001/XMLSchema"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
