from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Elem:
    class Meta:
        name = "elem"

    choice: List[object] = field(
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
                {
                    "name": "b3",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "b4",
                    "type": object,
                    "namespace": "",
                },
            ),
            "max_occurs": 4,
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
