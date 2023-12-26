from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-length-3-NS"


@dataclass
class NistschemaSvIvListDurationLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-length-3"
        namespace = "NISTSchema-SV-IV-list-duration-length-3-NS"

    value: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "length": 7,
            "tokens": True,
        },
    )
