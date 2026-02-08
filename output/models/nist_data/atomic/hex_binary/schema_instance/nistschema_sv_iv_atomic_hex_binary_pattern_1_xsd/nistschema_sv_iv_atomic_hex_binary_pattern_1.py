from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-pattern-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-pattern-1-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"[0-9A-F]{56}",
        },
    )
