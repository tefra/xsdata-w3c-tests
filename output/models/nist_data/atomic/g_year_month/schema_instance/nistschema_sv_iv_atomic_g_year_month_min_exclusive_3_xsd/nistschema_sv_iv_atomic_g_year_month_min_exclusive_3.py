from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-3-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": Period("2029-04"),
        }
    )
