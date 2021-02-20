from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-maxLength-3-NS"


@dataclass
class NistschemaSvIvListDateMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-date-maxLength-3-NS"

    value: List[XmlDate] = field(
        default_factory=list,
        metadata={
            "max_length": 7,
            "tokens": True,
        }
    )
