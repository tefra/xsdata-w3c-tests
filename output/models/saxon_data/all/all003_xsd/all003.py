from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Doc:
    """
    :ivar content:
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar d:
    """
    class Meta:
        name = "doc"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    a: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        }
    )
    b: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        }
    )
    c: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    d: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
