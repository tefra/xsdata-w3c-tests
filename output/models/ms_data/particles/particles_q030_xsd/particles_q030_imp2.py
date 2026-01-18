from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "bar"


@dataclass(kw_only=True)
class E1:
    class Meta:
        name = "e1"
        namespace = "bar"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class E2:
    class Meta:
        name = "e2"
        namespace = "bar"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ImpElem1:
    class Meta:
        name = "impElem1"
        namespace = "bar"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
