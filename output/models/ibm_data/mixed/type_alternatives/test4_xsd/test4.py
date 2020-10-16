from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Example:
    """
    :ivar x:
    :ivar kind:
    """
    x: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
