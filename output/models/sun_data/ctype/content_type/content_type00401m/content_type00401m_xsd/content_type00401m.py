from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "contentType"


@dataclass
class A1:
    class Meta:
        name = "A"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class A(A1):
    class Meta:
        name = "a"
        namespace = "contentType"
