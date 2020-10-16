from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "urn:test"


@dataclass
class Root:
    """
    :ivar content:
    :ivar a:
    :ivar b1:
    :ivar b2:
    :ivar b3:
    :ivar b4:
    :ivar b5:
    """
    class Meta:
        namespace = "urn:test"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    a: Optional[str] = field(
        default=None,
        metadata={
            "name": "A",
            "type": "Element",
            "required": True,
        }
    )
    b1: List[str] = field(
        default_factory=list,
        metadata={
            "name": "B1",
            "type": "Element",
            "max_occurs": 5,
        }
    )
    b2: List[str] = field(
        default_factory=list,
        metadata={
            "name": "B2",
            "type": "Element",
            "max_occurs": 5,
        }
    )
    b3: List[str] = field(
        default_factory=list,
        metadata={
            "name": "B3",
            "type": "Element",
            "max_occurs": 5,
        }
    )
    b4: List[str] = field(
        default_factory=list,
        metadata={
            "name": "B4",
            "type": "Element",
            "max_occurs": 5,
        }
    )
    b5: List[str] = field(
        default_factory=list,
        metadata={
            "name": "B5",
            "type": "Element",
            "max_occurs": 5,
        }
    )
