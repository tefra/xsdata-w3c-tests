from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-time-minExclusive-1-NS"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": XmlTime(0, 0, 0, 0),
        },
    )
