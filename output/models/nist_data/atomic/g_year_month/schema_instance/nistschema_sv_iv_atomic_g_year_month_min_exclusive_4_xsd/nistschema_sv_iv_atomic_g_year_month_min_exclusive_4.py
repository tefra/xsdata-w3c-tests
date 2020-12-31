from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-4-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": Period("1970-06"),
        }
    )
