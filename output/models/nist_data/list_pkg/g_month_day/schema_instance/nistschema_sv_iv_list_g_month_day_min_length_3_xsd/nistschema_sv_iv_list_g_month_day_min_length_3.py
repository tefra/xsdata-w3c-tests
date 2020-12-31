from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-minLength-3-NS"


@dataclass
class NistschemaSvIvListGMonthDayMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-minLength-3"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-minLength-3-NS"

    value: List[Period] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 7,
            "tokens": True,
        }
    )
