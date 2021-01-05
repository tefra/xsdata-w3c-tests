from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDurationMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-duration-minInclusive-2-NS"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlDuration("P1978Y12M21DT17H22M44S"),
        }
    )
