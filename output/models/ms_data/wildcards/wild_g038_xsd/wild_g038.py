from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://foobar"


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"
        namespace = "http://foobar"

    value: str = field(default="")


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    target_namespace_w3_org_1999_xhtml_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace http://www.w3.org/1999/xhtml",
        },
    )
