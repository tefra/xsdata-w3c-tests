from dataclasses import dataclass, field
from typing import List, Optional, Type, Union


@dataclass
class Elem:
    class Meta:
        name = "elem"

    choice: List[Union["Elem.E1", "Elem.E2", "Elem.E3", "Elem.E4"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": Type["Elem.E1"],
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "e2",
                    "type": Type["Elem.E2"],
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "e3",
                    "type": Type["Elem.E3"],
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "e4",
                    "type": Type["Elem.E4"],
                    "namespace": "",
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
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
    class E3:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class E4:
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
