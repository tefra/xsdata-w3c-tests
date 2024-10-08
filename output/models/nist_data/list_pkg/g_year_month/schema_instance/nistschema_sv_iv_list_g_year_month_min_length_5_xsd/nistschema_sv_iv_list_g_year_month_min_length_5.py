from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-minLength-5-NS"


@dataclass
class NistschemaSvIvListGYearMonthMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-minLength-5"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-minLength-5-NS"

    value: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "min_length": 10,
            "tokens": True,
        },
    )
