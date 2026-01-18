from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNegativeIntegerMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-3-NS"

    value: int = field(
        metadata={
            "required": True,
            "min_exclusive": -900435039333670416,
        }
    )
