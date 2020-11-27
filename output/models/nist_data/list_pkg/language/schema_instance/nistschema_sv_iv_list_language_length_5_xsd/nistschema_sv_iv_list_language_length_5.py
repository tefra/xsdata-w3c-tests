from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-language-length-5-NS"


@dataclass
class NistschemaSvIvListLanguageLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-language-length-5"
        namespace = "NISTSchema-SV-IV-list-language-length-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 10,
            "tokens": True,
        }
    )
