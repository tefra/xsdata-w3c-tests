from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://importedXSD"


@dataclass(kw_only=True)
class B:
    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    e2: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )


@dataclass(kw_only=True)
class ImpElem1(B):
    class Meta:
        name = "impElem1"
        namespace = "http://importedXSD"
