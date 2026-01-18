from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "urn:bar"


@dataclass(kw_only=True)
class Ct:
    class Meta:
        name = "ct"

    a: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Elem:
    class Meta:
        name = "elem"
        namespace = "urn:bar"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
