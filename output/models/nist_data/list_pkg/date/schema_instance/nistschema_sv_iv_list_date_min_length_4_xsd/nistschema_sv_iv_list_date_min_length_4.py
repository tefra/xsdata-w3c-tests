from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-minLength-4-NS"


@dataclass
class NistschemaSvIvListDateMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-minLength-4"
        namespace = "NISTSchema-SV-IV-list-date-minLength-4-NS"

    value: List[XmlDate] = field(
        default_factory=list,
        metadata={
            "min_length": 8,
            "tokens": True,
        }
    )
