from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDurationMaxExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxExclusive-1-NS"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "max_exclusive": XmlDuration("P1970Y01M01DT00H00M01S"),
        }
    )
