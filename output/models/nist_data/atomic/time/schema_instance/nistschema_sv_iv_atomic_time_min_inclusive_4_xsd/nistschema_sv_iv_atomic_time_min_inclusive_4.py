from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-time-minInclusive-4-NS"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlTime(19, 31, 35, 0),
        },
    )
