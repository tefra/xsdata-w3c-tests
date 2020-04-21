from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "publicId"


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"
        namespace = "publicId"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
