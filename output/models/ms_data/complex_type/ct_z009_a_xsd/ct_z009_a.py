from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    foo_or_sg: list[Root.Foo | Root.Sg] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": ForwardRef("Root.Foo"),
                    "namespace": "",
                },
                {
                    "name": "sg",
                    "type": ForwardRef("Root.Sg"),
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Foo:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class Sg:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )
