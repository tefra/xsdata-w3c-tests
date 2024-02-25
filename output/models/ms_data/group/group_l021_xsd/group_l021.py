from dataclasses import dataclass, field
from typing import List, Optional, Type, Union


@dataclass
class Elem:
    class Meta:
        name = "elem"

    b1_or_b2: List[Union["Elem.B1", "Elem.B2"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b1",
                    "type": Type["Elem.B1"],
                    "namespace": "",
                },
                {
                    "name": "b2",
                    "type": Type["Elem.B2"],
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
