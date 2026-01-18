from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-minExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonPositiveIntegerMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-minExclusive-4"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonPositiveInteger-minExclusive-4-NS"
        )

    value: int = field(
        metadata={
            "required": True,
            "min_exclusive": -594976296252018754,
        }
    )
