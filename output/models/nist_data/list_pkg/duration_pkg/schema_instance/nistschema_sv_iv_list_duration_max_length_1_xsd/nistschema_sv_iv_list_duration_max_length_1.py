from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import Duration

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-maxLength-1-NS"


@dataclass
class NistschemaSvIvListDurationMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-duration-maxLength-1-NS"

    value: List[Duration] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 5,
            "tokens": True,
        }
    )