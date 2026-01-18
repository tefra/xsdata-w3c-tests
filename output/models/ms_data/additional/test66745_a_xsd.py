from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"
        namespace = "foo"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Foo1(Foo):
    class Meta:
        name = "foo1"
        namespace = "foo1"

    x: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"
        namespace = "foo"

    foo1_or_foo_or_bar: list[Foo1 | Foo | Bar] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo1",
                    "type": Foo1,
                    "namespace": "foo1",
                },
                {
                    "name": "foo",
                    "type": Foo,
                },
                {
                    "name": "bar",
                    "type": ForwardRef("Bar"),
                },
            ),
        },
    )
