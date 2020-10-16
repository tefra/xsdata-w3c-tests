from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Doc:
    """
    :ivar content:
    :ivar att:
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
    att: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
