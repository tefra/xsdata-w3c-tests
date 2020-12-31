from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGYearMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gYear-minExclusive-4-NS"

    value: Optional[Period] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": Period("2012"),
        }
    )
