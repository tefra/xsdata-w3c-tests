from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-length-4-NS"


@dataclass
class NistschemaSvIvListGYearMonthLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-length-4"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-length-4-NS"

    value: List[Period] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 8,
            "tokens": True,
        }
    )
