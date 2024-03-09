from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-maxLength-4-NS"


@dataclass
class NistschemaSvIvListTimeMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-maxLength-4"
        namespace = "NISTSchema-SV-IV-list-time-maxLength-4-NS"

    value: List[XmlTime] = field(
        default_factory=list,
        metadata={
            "max_length": 8,
            "tokens": True,
        },
    )
