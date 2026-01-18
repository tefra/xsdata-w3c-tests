from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-pattern-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-duration-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"P20\d\dY\d3M\d1DT\d4H\d7M\d6S",
        },
    )
