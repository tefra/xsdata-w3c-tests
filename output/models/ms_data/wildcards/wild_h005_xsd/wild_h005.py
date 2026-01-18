from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://foobar"


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    target_namespace_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
            "process_contents": "skip",
        },
    )
