from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "IdConstrDefs/fields"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "IdConstrDefs/fields"

    number: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
