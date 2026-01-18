from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-pattern-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimePattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-time-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d0:3\d:2\d",
        },
    )
