from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-5-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": Period("2030-11"),
        }
    )
