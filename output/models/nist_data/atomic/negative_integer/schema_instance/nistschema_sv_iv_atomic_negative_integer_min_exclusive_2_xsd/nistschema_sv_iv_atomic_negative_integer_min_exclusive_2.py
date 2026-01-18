from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNegativeIntegerMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-2-NS"

    value: int = field(
        metadata={
            "required": True,
            "min_exclusive": -435976618086570511,
        }
    )
