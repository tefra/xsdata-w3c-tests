from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNegativeIntegerMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-4-NS"

    value: int = field(
        metadata={
            "min_exclusive": -495295756372066909,
        }
    )
