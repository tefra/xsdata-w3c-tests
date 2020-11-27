from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-maxLength-4-NS"


@dataclass
class NistschemaSvIvListFloatMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-float-maxLength-4"
        namespace = "NISTSchema-SV-IV-list-float-maxLength-4-NS"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 8,
            "tokens": True,
        }
    )
