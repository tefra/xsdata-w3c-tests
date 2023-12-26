from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "importNS"


@dataclass
class R:
    class Meta:
        name = "r"
        namespace = "importNS"

    val2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "importNS",
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
