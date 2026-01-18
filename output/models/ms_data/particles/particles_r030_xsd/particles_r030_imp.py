from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "bar"


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


@dataclass(kw_only=True)
class ImpElem2:
    class Meta:
        name = "impElem2"
        namespace = "bar"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
