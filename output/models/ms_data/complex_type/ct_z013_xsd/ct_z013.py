from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ns"


@dataclass
class Ct:
    """
    :ivar content:
    :ivar a:
    """
    class Meta:
        name = "CT"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    a: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class E(Ct):
    class Meta:
        name = "e"
        namespace = "ns"
