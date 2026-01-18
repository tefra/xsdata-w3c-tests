from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-pattern-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-gYear-pattern-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d\d47",
        },
    )
