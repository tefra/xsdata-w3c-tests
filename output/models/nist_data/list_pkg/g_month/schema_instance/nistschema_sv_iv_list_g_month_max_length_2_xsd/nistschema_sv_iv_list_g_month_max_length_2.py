from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-maxLength-2-NS"


@dataclass
class NistschemaSvIvListGMonthMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-maxLength-2"
        namespace = "NISTSchema-SV-IV-list-gMonth-maxLength-2-NS"

    value: List[Period] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 6,
            "tokens": True,
        }
    )
