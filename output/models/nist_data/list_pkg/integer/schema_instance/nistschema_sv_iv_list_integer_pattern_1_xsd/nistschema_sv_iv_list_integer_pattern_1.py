from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-integer-pattern-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListIntegerPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-integer-pattern-1"
        namespace = "NISTSchema-SV-IV-list-integer-pattern-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\-\d{18} \-\d{13} \-\d{9} \-\d{5} \-\d{1} \d{3} \d{7} \d{11} \d{18}",
            "tokens": True,
        },
    )
