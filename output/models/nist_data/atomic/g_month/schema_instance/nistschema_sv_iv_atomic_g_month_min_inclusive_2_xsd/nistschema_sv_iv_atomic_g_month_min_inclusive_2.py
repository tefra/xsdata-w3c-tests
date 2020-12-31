from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicGMonthMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-minInclusive-2-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Period("--05"),
        }
    )
