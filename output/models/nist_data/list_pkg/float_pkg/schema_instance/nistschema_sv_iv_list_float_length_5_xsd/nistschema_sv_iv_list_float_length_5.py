from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-length-5-NS"


@dataclass
class NistschemaSvIvListFloatLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-float-length-5"
        namespace = "NISTSchema-SV-IV-list-float-length-5-NS"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 10,
            "tokens": True,
        }
    )
