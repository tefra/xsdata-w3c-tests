from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Elem:
    class Meta:
        name = "elem"

    b1_or_b2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b1",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "b2",
                    "type": object,
                    "namespace": "",
                },
            ),
            "max_occurs": 99999999999999,
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: Optional[Elem] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
