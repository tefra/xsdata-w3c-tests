from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "a"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    version: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "element",
                    "type": str,
                },
            ),
        },
    )
