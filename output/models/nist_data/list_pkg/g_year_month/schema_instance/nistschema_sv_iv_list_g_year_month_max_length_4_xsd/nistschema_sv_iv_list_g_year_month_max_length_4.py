from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-maxLength-4-NS"


@dataclass
class NistschemaSvIvListGYearMonthMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-maxLength-4"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-maxLength-4-NS"

    value: List[Period] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 8,
            "tokens": True,
        }
    )
