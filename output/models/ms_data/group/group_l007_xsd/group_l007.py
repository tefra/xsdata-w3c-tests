from dataclasses import dataclass, field
from typing import List, Optional, Type


@dataclass
class Elem:
    class Meta:
        name = "elem"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
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
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class B2:
        value: Optional[str] = field(
            default=None,
            metadata={
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
