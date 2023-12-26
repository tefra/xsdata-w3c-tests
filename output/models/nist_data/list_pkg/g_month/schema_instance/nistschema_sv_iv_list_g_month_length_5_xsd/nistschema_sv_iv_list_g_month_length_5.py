from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-length-5-NS"


@dataclass
class NistschemaSvIvListGMonthLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-length-5"
        namespace = "NISTSchema-SV-IV-list-gMonth-length-5-NS"

    value: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "length": 10,
            "tokens": True,
        },
    )
