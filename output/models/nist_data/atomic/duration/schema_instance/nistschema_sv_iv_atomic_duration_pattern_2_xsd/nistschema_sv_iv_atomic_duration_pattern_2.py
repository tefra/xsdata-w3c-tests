from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-pattern-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-duration-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"P\d\d74Y0\dM\d6DT1\dH\d0M\d7S",
        },
    )
