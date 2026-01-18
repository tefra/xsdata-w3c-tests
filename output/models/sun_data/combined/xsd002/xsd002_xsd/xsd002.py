from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://foo.com"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://foo.com"

    foo_or_bar_or_zot: list[Root.Foo | Root.Bar | Root.Zot] = field(
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
                    "name": "bar",
                    "type": ForwardRef("Root.Bar"),
                },
                {
                    "name": "zot",
                    "type": ForwardRef("Root.Zot"),
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
    class Bar:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
            },
        )

    @dataclass(kw_only=True)
    class Zot:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )
