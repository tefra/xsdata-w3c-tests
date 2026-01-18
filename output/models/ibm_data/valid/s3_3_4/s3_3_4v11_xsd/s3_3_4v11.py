from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    union_of_ids: list[int | str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    idref: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
