from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-1-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": Period("1970-01"),
        }
    )
