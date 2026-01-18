from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class B:
    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    e2: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class R:
    e1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    e2: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: None | R = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
