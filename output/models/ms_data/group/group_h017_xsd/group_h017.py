from dataclasses import dataclass, field
from typing import List, Optional, Type, Union


@dataclass
class A:
    choice: List[Union["A.X1", "A.X2", "A.Y1", "A.Y2"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "x1",
                    "type": Type["A.X1"],
                    "namespace": "",
                    "max_occurs": 8,
                },
                {
                    "name": "x2",
                    "type": Type["A.X2"],
                    "namespace": "",
                    "max_occurs": 8,
                },
                {
                    "name": "y1",
                    "type": Type["A.Y1"],
                    "namespace": "",
                    "max_occurs": 4,
                },
                {
                    "name": "y2",
                    "type": Type["A.Y2"],
                    "namespace": "",
                    "max_occurs": 4,
                },
            ),
            "max_occurs": 16,
        },
    )

    @dataclass
    class X1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class X2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class Y1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class Y2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )


@dataclass
class Elem(A):
    class Meta:
        name = "elem"


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
