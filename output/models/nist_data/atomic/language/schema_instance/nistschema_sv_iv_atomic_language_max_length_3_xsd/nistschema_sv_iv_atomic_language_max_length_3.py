from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-maxLength-3-NS"


@dataclass
class NistschemaSvIvAtomicLanguageMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-maxLength-3"
        namespace = "NISTSchema-SV-IV-atomic-language-maxLength-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_length": 2,
        }
    )
