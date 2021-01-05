from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-minLength-3-NS"


@dataclass
class NistschemaSvIvListGYearMonthMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-minLength-3"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-minLength-3-NS"

    value: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 7,
            "tokens": True,
        }
    )
