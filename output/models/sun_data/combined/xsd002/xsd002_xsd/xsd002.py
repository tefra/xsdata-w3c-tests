from dataclasses import dataclass, field
from typing import List, Optional, Type, Union

__NAMESPACE__ = "http://foo.com"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://foo.com"

    foo_or_bar_or_zot: List[Union["Root.Foo", "Root.Bar", "Root.Zot"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": Type["Root.Foo"],
                    "namespace": "",
                },
                {
                    "name": "bar",
                    "type": Type["Root.Bar"],
                },
                {
                    "name": "zot",
                    "type": Type["Root.Zot"],
                    "namespace": "",
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
                "namespace": "",
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

    @dataclass
    class Zot:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )
