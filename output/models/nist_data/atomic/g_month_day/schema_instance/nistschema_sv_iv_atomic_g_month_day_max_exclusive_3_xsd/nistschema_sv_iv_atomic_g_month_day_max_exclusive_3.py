from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-maxExclusive-3-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": Period("--07-23"),
        }
    )
