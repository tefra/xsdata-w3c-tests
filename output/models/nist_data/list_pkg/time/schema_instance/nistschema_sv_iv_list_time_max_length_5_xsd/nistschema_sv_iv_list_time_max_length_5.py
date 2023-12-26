from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-maxLength-5-NS"


@dataclass
class NistschemaSvIvListTimeMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-time-maxLength-5-NS"

    value: List[XmlTime] = field(
        default_factory=list,
        metadata={
            "max_length": 10,
            "tokens": True,
        },
    )
