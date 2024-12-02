from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    x_or_y: list[Union["Doc.X", "Doc.Y"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "x",
                    "type": ForwardRef("Doc.X"),
                },
                {
                    "name": "y",
                    "type": ForwardRef("Doc.Y"),
                },
            ),
            "max_occurs": 2,
        },
    )

    @dataclass
    class X:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "required": True,
            },
        )

    @dataclass
    class Y:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "required": True,
            },
        )
