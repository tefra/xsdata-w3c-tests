from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-time-minInclusive-2-NS"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlTime(21, 11, 44, 0),
        }
    )
