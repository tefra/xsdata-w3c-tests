from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "contentType"


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"
        namespace = "contentType"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
