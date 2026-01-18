from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-Name-pattern-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListNamePattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-Name-pattern-3"
        namespace = "NISTSchema-SV-IV-list-Name-pattern-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\i\c{24} \i\c{23} \i\c{57} \i\c{50} \i\c{52} \i\c{35} \i\c{28}",
            "tokens": True,
        },
    )
