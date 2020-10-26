from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class B:
    """
    :ivar x:
    """
    x: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Elem(B):
    """
    :ivar a1_or_a2:
    """
    class Meta:
        name = "elem"

    a1_or_a2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "A1",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "A2",
                    "type": object,
                    "namespace": "",
                },
            ),
            "max_occurs": 999999999999999,
        }
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: Optional[Elem] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
