from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-time-minInclusive-3-NS"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlTime(1, 3, 8, 0),
        },
    )
