from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-maxLength-5-NS"


@dataclass
class NistschemaSvIvListGYearMonthMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-maxLength-5-NS"

    value: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 10,
            "tokens": True,
        }
    )
