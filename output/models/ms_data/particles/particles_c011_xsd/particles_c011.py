from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class AnyType:
    class Meta:
        name = "any"

    xslt_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://xslt",
            "max_occurs": 4,
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


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: list[AnyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 100,
        },
    )
