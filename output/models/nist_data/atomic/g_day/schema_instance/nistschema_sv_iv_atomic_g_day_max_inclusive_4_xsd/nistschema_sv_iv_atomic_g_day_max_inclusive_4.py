from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGDayMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gDay-maxInclusive-4-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": Period("---10"),
        }
    )
