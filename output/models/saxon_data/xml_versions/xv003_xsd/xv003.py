from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Doc:
    class Meta:
        name = "doc"

    att: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
