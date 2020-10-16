from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "d"


@dataclass
class D:
    """
    :ivar d:
    """
    class Meta:
        name = "d"

    d: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "d",
            "required": True,
        }
    )
