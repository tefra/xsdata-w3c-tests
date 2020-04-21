from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "b"


@dataclass
class B:
    """
    :ivar b:
    """
    class Meta:
        name = "b"

    b: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="b",
            required=True
        )
    )
