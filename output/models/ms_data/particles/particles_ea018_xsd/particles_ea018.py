from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    a1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    a2: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    a5: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    a4: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    a3: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
