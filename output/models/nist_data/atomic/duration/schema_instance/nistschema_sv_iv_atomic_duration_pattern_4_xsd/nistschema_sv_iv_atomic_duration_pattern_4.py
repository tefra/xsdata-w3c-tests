from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-pattern-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-duration-pattern-4-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"P19\d\dY\d8M\d3DT\d0H1\dM\d2S",
        },
    )
