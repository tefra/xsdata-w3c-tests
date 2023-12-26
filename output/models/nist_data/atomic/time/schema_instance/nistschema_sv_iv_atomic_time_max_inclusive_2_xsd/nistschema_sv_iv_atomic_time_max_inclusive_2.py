from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicTimeMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-time-maxInclusive-2-NS"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": XmlTime(13, 46, 8, 0),
        },
    )
