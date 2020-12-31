from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicGYearMaxInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-1-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": Period("1970"),
        }
    )
