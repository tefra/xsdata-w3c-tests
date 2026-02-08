from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-maxExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntegerMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-integer-maxExclusive-3-NS"

    value: int = field(
        metadata={
            "max_exclusive": 549869808681548999,
        }
    )
