from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-pattern-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDatePattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-date-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d\d90-\d7-2\d",
        },
    )
