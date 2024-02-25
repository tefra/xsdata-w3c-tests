from dataclasses import dataclass, field
from typing import Optional, Type, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    a_or_b: Optional[Union["Doc.A", "Doc.B"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": Type["Doc.A"],
                },
                {
                    "name": "b",
                    "type": Type["Doc.B"],
                },
            ),
        },
    )

    @dataclass
    class A:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "required": True,
            },
        )

    @dataclass
    class B:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "required": True,
            },
        )
