from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGMonthDayPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"--\d2-1\d",
        },
    )
