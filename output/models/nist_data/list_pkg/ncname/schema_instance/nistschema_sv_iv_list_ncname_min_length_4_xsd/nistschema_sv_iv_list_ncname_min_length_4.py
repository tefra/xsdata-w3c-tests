from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-NCName-minLength-4-NS"


@dataclass
class NistschemaSvIvListNcnameMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-NCName-minLength-4"
        namespace = "NISTSchema-SV-IV-list-NCName-minLength-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "min_length": 8,
            "tokens": True,
        },
    )
