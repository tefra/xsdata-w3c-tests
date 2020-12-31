from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-5-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": Period("2030-12"),
        }
    )
