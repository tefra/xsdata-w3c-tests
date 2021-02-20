from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-anyURI-maxLength-5-NS"


@dataclass
class NistschemaSvIvListAnyUriMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-anyURI-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-anyURI-maxLength-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "max_length": 10,
            "tokens": True,
        }
    )
