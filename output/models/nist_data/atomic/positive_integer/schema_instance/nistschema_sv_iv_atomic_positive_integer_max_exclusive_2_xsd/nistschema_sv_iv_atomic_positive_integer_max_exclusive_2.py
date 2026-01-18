from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicPositiveIntegerMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-2-NS"

    value: int = field(
        metadata={
            "required": True,
            "max_exclusive": 32371283896903692,
        }
    )
