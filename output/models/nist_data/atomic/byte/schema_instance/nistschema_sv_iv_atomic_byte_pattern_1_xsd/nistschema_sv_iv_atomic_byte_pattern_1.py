from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-pattern-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBytePattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-byte-pattern-1-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\-\d{3}",
        },
    )
