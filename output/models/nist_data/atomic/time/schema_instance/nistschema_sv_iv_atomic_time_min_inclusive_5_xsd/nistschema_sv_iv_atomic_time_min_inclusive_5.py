from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-time-minInclusive-5-NS"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlTime(23, 59, 59, 0),
        },
    )
