from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import Duration

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-minLength-3-NS"


@dataclass
class NistschemaSvIvListDurationMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-minLength-3"
        namespace = "NISTSchema-SV-IV-list-duration-minLength-3-NS"

    value: List[Duration] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 7,
            "tokens": True,
        }
    )
