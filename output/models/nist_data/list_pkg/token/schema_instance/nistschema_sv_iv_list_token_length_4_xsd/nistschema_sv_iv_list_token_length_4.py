from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-token-length-4-NS"


@dataclass
class NistschemaSvIvListTokenLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-token-length-4"
        namespace = "NISTSchema-SV-IV-list-token-length-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "length": 8,
            "tokens": True,
        },
    )
