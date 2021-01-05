from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-minLength-5-NS"


@dataclass
class NistschemaSvIvListDateMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-minLength-5"
        namespace = "NISTSchema-SV-IV-list-date-minLength-5-NS"

    value: List[XmlDate] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 10,
            "tokens": True,
        }
    )
