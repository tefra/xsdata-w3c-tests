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
                },
                {
                    "name": "x2",
                    "type": Type["A.X2"],
                    "namespace": "",
                },
                {
                    "name": "y1",
                    "type": Type["A.Y1"],
                    "namespace": "",
                },
                {
                    "name": "y2",
                    "type": Type["A.Y2"],
                    "namespace": "",
                },
            ),
            "max_occurs": 8,
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

    choice: List[Union["Elem.X1", "Elem.X2", "Elem.Y1", "Elem.Y2"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "x1",
                    "type": Type["Elem.X1"],
                    "namespace": "",
                },
                {
                    "name": "x2",
                    "type": Type["Elem.X2"],
                    "namespace": "",
                },
                {
                    "name": "y1",
                    "type": Type["Elem.Y1"],
                    "namespace": "",
                },
                {
                    "name": "y2",
                    "type": Type["Elem.Y2"],
                    "namespace": "",
                },
            ),
            "max_occurs": 6,
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
