from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "particles"


@dataclass
class A:
    """
    :ivar date:
    """
    class Meta:
        name = "a"
        namespace = "particles"

    date: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
