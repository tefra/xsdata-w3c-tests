from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-length-4-NS"


@dataclass
class NistschemaSvIvListTimeLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-length-4"
        namespace = "NISTSchema-SV-IV-list-time-length-4-NS"

    value: List[XmlTime] = field(
        default_factory=list,
        metadata={
            "length": 8,
            "tokens": True,
        },
    )
