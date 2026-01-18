from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"
        namespace = "http://xsdtesting"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    other_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    a_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "A",
        },
    )
