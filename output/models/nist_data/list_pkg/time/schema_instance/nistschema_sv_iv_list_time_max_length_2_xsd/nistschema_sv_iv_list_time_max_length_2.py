from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-maxLength-2-NS"


@dataclass
class NistschemaSvIvListTimeMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-maxLength-2"
        namespace = "NISTSchema-SV-IV-list-time-maxLength-2-NS"

    value: List[XmlTime] = field(
        default_factory=list,
        metadata={
            "max_length": 6,
            "tokens": True,
        },
    )
