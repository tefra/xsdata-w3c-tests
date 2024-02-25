from dataclasses import dataclass, field
from typing import List, Optional, Type, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    foo_or_bar: List[Union["Doc.Foo", "Doc.Bar"]] = field(
        default_factory=list,
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
