from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-minLength-5-NS"


@dataclass
class NistschemaSvIvListFloatMinLength5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-float-minLength-5"
        namespace = "NISTSchema-SV-IV-list-float-minLength-5-NS"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 10,
            "tokens": True,
        }
    )
