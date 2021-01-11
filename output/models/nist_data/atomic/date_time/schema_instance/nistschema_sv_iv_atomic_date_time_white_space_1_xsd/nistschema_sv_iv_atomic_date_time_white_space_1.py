from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-whiteSpace-1-NS"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
