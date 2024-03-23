from dataclasses import dataclass, field
from typing import List, Optional, Type, Union

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
                    "type": Type["Doc.A"],
                    "max_occurs": 2,
                },
                {
                    "name": "b",
                    "type": Type["Doc.B"],
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
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
