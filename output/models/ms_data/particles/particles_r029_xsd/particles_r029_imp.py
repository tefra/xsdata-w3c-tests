from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class ImpElem1:
    class Meta:
        name = "impElem1"
        namespace = "foo"

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
        namespace = "foo"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
