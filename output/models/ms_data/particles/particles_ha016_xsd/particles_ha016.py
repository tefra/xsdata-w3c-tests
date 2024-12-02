from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    foo_or_bar: list[Union["Doc.Foo", "Doc.Bar"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": ForwardRef("Doc.Foo"),
                },
                {
                    "name": "bar",
                    "type": ForwardRef("Doc.Bar"),
                },
            ),
            "max_occurs": 2,
        },
    )

    @dataclass
    class Foo:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "required": True,
            },
        )

    @dataclass
    class Bar:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "required": True,
            },
        )
