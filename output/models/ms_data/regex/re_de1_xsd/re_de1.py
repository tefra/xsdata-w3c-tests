from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"\p{Nd}{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
