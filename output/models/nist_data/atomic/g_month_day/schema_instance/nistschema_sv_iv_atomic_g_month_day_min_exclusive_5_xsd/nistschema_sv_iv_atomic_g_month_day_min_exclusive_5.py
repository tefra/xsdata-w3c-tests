from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-minExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-minExclusive-5-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": Period("--12-30"),
        }
    )
