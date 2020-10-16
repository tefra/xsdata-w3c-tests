from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class Root:
    """
    :ivar ele11:
    """
    class Meta:
        name = "root"
        namespace = "a"

    ele11: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
