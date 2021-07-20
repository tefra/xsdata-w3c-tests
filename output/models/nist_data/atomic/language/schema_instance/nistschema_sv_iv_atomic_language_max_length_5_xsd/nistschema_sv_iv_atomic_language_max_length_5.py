from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-maxLength-5-NS"


@dataclass
class NistschemaSvIvAtomicLanguageMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-maxLength-5"
        namespace = "NISTSchema-SV-IV-atomic-language-maxLength-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "max_length": 11,
        }
    )
