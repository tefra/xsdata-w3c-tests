from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class Elem:
    class Meta:
        name = "elem"

    choice: Optional[Union["Elem.B1", "Elem.B2", "Elem.B3", "Elem.B4"]] = (
        field(
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
                    {
                        "name": "b3",
                        "type": ForwardRef("Elem.B3"),
                        "namespace": "",
                    },
                    {
                        "name": "b4",
                        "type": ForwardRef("Elem.B4"),
                        "namespace": "",
                    },
                ),
            },
        )
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
    class B3:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class B4:
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
