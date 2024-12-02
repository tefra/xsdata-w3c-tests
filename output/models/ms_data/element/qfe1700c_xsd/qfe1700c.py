from dataclasses import dataclass, field
from typing import Optional


@dataclass
class E2:
    class Meta:
        name = "e2"
        nillable = True

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "e3",
                    "type": int,
                    "namespace": "",
                },
            ),
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    e1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )
    e2: Optional[E2] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
