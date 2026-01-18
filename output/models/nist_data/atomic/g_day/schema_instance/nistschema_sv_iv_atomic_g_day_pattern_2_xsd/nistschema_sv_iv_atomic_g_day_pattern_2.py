from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-pattern-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGDayPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-gDay-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"---\d5",
        },
    )
