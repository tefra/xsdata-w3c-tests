from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": 571841216500225568,
        }
    )
