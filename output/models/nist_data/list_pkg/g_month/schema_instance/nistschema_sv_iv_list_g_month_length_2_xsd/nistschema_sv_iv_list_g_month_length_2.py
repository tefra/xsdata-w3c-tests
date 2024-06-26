from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-length-2-NS"


@dataclass
class NistschemaSvIvListGMonthLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-length-2"
        namespace = "NISTSchema-SV-IV-list-gMonth-length-2-NS"

    value: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "length": 6,
            "tokens": True,
        },
    )
