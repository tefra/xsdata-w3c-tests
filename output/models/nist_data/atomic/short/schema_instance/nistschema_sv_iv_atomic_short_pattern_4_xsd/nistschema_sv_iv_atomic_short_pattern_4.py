from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-pattern-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicShortPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-short-pattern-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{2}",
        },
    )
