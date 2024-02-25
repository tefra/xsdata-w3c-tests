from dataclasses import dataclass, field
from typing import List, Optional, Type, Union


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_or_sg: List[Union["Root.Foo", "Root.Sg"]] = field(
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
                    "name": "sg",
                    "type": Type["Root.Sg"],
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
    class Sg:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )
