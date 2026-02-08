from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-minExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicPositiveIntegerMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-minExclusive-4-NS"

    value: int = field(
        metadata={
            "min_exclusive": 506558727413711217,
        }
    )
