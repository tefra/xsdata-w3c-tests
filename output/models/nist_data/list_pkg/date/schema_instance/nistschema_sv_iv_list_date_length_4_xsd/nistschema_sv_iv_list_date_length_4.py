from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-length-4-NS"


@dataclass
class NistschemaSvIvListDateLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-length-4"
        namespace = "NISTSchema-SV-IV-list-date-length-4-NS"

    value: List[XmlDate] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 8,
            "tokens": True,
        }
    )
