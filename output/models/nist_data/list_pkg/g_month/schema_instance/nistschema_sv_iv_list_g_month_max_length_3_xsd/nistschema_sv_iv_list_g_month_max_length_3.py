from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-maxLength-3-NS"


@dataclass
class NistschemaSvIvListGMonthMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-gMonth-maxLength-3-NS"

    value: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "max_length": 7,
            "tokens": True,
        },
    )
