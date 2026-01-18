from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-pattern-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListNmtokensPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-pattern-3"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-pattern-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\c{20} \c{48} \c{3} \c{54} \c{13} \c{29} \c{5}",
            "tokens": True,
        },
    )
