from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-maxLength-1-NS"


@dataclass
class NistschemaSvIvListDurationMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-duration-maxLength-1-NS"

    value: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "max_length": 5,
            "tokens": True,
        },
    )
