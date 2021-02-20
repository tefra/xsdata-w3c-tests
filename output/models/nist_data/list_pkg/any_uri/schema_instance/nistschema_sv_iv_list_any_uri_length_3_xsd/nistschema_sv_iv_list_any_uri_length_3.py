from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-anyURI-length-3-NS"


@dataclass
class NistschemaSvIvListAnyUriLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-anyURI-length-3"
        namespace = "NISTSchema-SV-IV-list-anyURI-length-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "length": 7,
            "tokens": True,
        }
    )
