from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    a_or_b: List[Union["Doc.A", "Doc.B"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": ForwardRef("Doc.A"),
                    "max_occurs": 4,
                },
                {
                    "name": "b",
                    "type": ForwardRef("Doc.B"),
                    "max_occurs": 4,
                },
            ),
            "max_occurs": 4,
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
