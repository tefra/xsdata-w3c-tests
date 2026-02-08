from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-minInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicByteMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-byte-minInclusive-4-NS"

    value: int = field(
        metadata={
            "min_inclusive": -50,
        }
    )
