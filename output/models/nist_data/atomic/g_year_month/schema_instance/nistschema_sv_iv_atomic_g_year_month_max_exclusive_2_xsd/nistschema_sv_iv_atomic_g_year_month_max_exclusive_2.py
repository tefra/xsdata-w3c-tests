from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-2-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": Period("1983-06"),
        }
    )
