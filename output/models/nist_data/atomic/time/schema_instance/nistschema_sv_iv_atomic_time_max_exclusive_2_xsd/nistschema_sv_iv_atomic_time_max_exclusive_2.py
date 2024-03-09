from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicTimeMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-time-maxExclusive-2-NS"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": XmlTime(8, 19, 11, 0),
        },
    )
