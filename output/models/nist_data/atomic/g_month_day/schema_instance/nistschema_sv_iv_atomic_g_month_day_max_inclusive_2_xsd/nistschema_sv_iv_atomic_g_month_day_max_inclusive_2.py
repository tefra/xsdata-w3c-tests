from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-maxInclusive-2-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": Period("--02-24"),
        }
    )
