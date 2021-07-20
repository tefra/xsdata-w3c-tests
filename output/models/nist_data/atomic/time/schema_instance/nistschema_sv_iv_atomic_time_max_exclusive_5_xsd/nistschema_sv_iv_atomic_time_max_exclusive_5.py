from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicTimeMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-time-maxExclusive-5-NS"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "max_exclusive": XmlTime(23, 59, 59, 0),
        }
    )
