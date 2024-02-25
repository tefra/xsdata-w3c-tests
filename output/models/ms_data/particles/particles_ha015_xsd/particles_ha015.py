from dataclasses import dataclass, field
from typing import Optional, Type, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    foo_or_bar: Optional[Union["Doc.Foo", "Doc.Bar"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": Type["Doc.Foo"],
                },
                {
                    "name": "bar",
                    "type": Type["Doc.Bar"],
                },
            ),
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
