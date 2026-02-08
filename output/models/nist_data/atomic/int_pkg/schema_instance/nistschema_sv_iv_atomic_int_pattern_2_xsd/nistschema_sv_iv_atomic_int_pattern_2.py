from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-pattern-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-int-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\-\d{5}",
        },
    )
