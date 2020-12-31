from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicGDayMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-gDay-minExclusive-1-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": Period("---01"),
        }
    )
