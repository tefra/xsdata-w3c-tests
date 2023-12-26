from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicTimeMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-time-maxInclusive-4-NS"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": XmlTime(18, 6, 59, 0),
        },
    )
