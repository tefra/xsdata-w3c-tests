from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Doc:
    class Meta:
        name = "doc"

    att1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    foo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
