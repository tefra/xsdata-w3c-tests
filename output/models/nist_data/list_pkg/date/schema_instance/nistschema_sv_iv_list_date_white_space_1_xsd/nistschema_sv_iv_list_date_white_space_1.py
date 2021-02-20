from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListDateWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-date-whiteSpace-1-NS"

    value: List[XmlDate] = field(
        default_factory=list,
        metadata={
            "white_space": "collapse",
            "tokens": True,
        }
    )
