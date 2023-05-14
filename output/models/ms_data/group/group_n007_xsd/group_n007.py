from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Elem:
    class Meta:
        name = "elem"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a1",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "a2",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "a3",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "a4",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "a5",
                    "type": object,
                    "namespace": "",
                },
            ),
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
