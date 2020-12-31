from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicGMonthMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-minExclusive-2-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": Period("--09"),
        }
    )
