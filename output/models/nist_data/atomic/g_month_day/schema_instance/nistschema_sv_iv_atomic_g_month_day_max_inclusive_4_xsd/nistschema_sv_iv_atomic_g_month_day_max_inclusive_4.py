from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-maxInclusive-4-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": Period("--07-01"),
        }
    )
