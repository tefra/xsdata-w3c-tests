from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-minInclusive-4-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Period("--03-04"),
        }
    )
