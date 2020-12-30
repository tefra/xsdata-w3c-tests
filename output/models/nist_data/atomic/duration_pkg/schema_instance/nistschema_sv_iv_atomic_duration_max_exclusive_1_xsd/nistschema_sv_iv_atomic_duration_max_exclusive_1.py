from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Duration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDurationMaxExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxExclusive-1-NS"

    value: Optional[Duration] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": Duration("P1970Y01M01DT00H00M01S"),
        }
    )
