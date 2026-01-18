from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKEN-pattern-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListNmtokenPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKEN-pattern-2"
        namespace = "NISTSchema-SV-IV-list-NMTOKEN-pattern-2-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\c{20} \c{60} \c{47} \c{22} \c{42} \c{14}",
            "tokens": True,
        },
    )
