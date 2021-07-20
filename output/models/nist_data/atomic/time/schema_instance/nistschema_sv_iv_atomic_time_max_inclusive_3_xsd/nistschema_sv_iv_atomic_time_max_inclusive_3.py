from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicTimeMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-time-maxInclusive-3-NS"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "max_inclusive": XmlTime(5, 7, 34, 0),
        }
    )
