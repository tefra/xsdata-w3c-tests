from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicTimeWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-time-whiteSpace-1-NS"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
            "white_space": "collapse",
        },
    )
