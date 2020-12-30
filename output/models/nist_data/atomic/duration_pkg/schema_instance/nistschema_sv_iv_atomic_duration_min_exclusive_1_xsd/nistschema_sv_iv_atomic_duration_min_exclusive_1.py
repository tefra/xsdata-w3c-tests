from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Duration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDurationMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-duration-minExclusive-1-NS"

    value: Optional[Duration] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": Duration("P1970Y01M01DT00H00M00S"),
        }
    )
