from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Duration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDurationMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-duration-minExclusive-3-NS"

    value: Optional[Duration] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": Duration("P2030Y05M22DT14H53M02S"),
        }
    )