from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicTimeMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-time-maxExclusive-4-NS"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": XmlTime(12, 25, 37, 0),
        }
    )
