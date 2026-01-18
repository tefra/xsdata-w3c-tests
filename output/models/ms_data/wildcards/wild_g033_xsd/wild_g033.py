from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://foobar"


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"
        namespace = "http://foobar"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    local_foobar_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local http://foobar",
        },
    )
