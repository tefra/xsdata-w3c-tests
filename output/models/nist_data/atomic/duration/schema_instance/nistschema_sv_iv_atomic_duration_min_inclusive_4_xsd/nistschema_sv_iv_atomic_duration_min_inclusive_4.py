from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDurationMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-duration-minInclusive-4-NS"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlDuration("P2024Y01M12DT09H17M54S"),
        }
    )
