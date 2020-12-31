from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGYearMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gYear-minInclusive-4-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Period("1997"),
        }
    )
