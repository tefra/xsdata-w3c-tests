from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-time-minExclusive-3-NS"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": XmlTime(13, 38, 10, 0),
        }
    )
