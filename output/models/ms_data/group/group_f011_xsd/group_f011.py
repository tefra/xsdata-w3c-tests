from dataclasses import dataclass, field
from typing import Optional, Type, Union


@dataclass
class B:
    x: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Elem(B):
    class Meta:
        name = "elem"

    a1_or_a2: Optional[Union["Elem.A1", "Elem.A2"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "A1",
                    "type": Type["Elem.A1"],
                    "namespace": "",
                },
                {
                    "name": "A2",
                    "type": Type["Elem.A2"],
                    "namespace": "",
                },
            ),
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
