from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class Elem:
    class Meta:
        name = "elem"

    b1_or_b2: Optional[Union["Elem.B1", "Elem.B2"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b1",
                    "type": ForwardRef("Elem.B1"),
                    "namespace": "",
                },
                {
                    "name": "b2",
                    "type": ForwardRef("Elem.B2"),
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass
    class B1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class B2:
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
