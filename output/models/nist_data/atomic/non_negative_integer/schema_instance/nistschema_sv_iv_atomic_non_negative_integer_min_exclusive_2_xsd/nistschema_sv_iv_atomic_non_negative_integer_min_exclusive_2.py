from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonNegativeIntegerMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minExclusive-2"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonNegativeInteger-minExclusive-2-NS"
        )

    value: int = field(
        metadata={
            "required": True,
            "min_exclusive": 279497457259986536,
        }
    )
