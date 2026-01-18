from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKEN-pattern-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListNmtokenPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKEN-pattern-1"
        namespace = "NISTSchema-SV-IV-list-NMTOKEN-pattern-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\c{40} \c{21} \c{50} \c{36} \c{35} \c{42} \c{54} \c{48}",
            "tokens": True,
        },
    )
