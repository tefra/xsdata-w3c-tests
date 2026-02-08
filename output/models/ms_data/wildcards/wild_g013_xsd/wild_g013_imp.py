from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/1999/xhtml"


@dataclass(kw_only=True)
class B:
    class Meta:
        name = "b"
        namespace = "http://www.w3.org/1999/xhtml"

    value: str = field(default="")


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://www.w3.org/1999/xhtml"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
