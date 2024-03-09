from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-time-minExclusive-4-NS"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": XmlTime(18, 16, 28, 0),
        },
    )
