from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicTimeMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-time-maxExclusive-3-NS"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": XmlTime(23, 35, 2, 0),
        },
    )
