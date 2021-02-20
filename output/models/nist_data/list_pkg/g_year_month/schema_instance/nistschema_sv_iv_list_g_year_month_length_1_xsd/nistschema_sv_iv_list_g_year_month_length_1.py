from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-length-1-NS"


@dataclass
class NistschemaSvIvListGYearMonthLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-length-1"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-length-1-NS"

    value: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "length": 5,
            "tokens": True,
        }
    )
