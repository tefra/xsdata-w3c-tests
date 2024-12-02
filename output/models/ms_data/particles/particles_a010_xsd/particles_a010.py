from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class Elem:
    class Meta:
        name = "elem"

    e1_or_e2: list[Union["Elem.E1", "Elem.E2"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": ForwardRef("Elem.E1"),
                    "namespace": "",
                    "max_occurs": 3,
                },
                {
                    "name": "e2",
                    "type": ForwardRef("Elem.E2"),
                    "namespace": "",
                    "max_occurs": 3,
                },
            ),
            "min_occurs": 2,
            "max_occurs": 3,
        },
    )

    @dataclass
    class E1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class E2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: Optional[Elem] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
