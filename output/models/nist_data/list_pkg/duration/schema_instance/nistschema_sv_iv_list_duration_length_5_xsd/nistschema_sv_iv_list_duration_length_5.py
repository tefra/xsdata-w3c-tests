from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-length-5-NS"


@dataclass
class NistschemaSvIvListDurationLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-length-5"
        namespace = "NISTSchema-SV-IV-list-duration-length-5-NS"

    value: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 10,
            "tokens": True,
        }
    )
