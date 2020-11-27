from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "a"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    element: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    version: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
