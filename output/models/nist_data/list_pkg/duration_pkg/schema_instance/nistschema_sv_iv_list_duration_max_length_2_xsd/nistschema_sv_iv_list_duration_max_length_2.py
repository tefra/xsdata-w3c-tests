from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import Duration

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-maxLength-2-NS"


@dataclass
class NistschemaSvIvListDurationMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-maxLength-2"
        namespace = "NISTSchema-SV-IV-list-duration-maxLength-2-NS"

    value: List[Duration] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 6,
            "tokens": True,
        }
    )