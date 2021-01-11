from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListDateTimeWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-dateTime-whiteSpace-1-NS"

    value: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "required": True,
            "white_space": "collapse",
            "tokens": True,
        }
    )
