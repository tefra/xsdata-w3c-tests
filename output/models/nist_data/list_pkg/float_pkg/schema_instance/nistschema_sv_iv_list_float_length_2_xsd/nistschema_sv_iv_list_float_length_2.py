from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-length-2-NS"


@dataclass
class NistschemaSvIvListFloatLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-float-length-2"
        namespace = "NISTSchema-SV-IV-list-float-length-2-NS"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "length": 6,
            "tokens": True,
        }
    )
