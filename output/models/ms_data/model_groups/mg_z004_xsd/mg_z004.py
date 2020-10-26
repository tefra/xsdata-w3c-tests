from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "urn:test"


@dataclass
class Root:
    """
    :ivar content:
    :ivar a:
    :ivar choice:
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
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "B1",
                    "type": str,
                },
                {
                    "name": "B2",
                    "type": str,
                },
                {
                    "name": "B3",
                    "type": str,
                },
                {
                    "name": "B4",
                    "type": str,
                },
                {
                    "name": "B5",
                    "type": str,
                },
            ),
            "max_occurs": 5,
        }
    )
