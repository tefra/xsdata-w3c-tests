from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union


@dataclass
class Elem:
    class Meta:
        name = "elem"

    a1_or_a2: List[Union["Elem.A1", "Elem.A2"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a1",
                    "type": ForwardRef("Elem.A1"),
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "a2",
                    "type": ForwardRef("Elem.A2"),
                    "namespace": "",
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )

    @dataclass
    class A1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class A2:
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
            "required": True,
        },
    )
