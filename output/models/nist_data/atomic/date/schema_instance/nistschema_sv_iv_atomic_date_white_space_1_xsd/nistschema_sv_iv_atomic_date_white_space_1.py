from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicDateWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-date-whiteSpace-1-NS"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
            "white_space": "collapse",
        },
    )
