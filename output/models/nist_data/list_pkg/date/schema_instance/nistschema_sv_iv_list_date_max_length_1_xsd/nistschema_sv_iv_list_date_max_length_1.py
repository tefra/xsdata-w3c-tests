from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-maxLength-1-NS"


@dataclass
class NistschemaSvIvListDateMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-date-maxLength-1-NS"

    value: List[XmlDate] = field(
        default_factory=list,
        metadata={
            "max_length": 5,
            "tokens": True,
        },
    )
