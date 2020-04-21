from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xyz"


@dataclass
class X:
    """
    :ivar message:
    """
    class Meta:
        namespace = "http://xyz"

    message: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
