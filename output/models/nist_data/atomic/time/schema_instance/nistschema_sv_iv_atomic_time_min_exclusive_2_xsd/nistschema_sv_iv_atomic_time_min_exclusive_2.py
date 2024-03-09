from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-time-minExclusive-2-NS"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": XmlTime(2, 57, 29, 0),
        },
    )
