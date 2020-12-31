from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-3-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": Period("1986-01"),
        }
    )
