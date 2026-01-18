from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "IdConstrDefs/annotation"


@dataclass(kw_only=True)
class People:
    class Meta:
        name = "people"
        namespace = "IdConstrDefs/annotation"

    person: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "IdConstrDefs/annotation"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
