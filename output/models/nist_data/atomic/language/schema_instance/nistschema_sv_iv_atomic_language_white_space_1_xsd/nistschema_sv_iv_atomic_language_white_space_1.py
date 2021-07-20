from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicLanguageWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-language-whiteSpace-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "white_space": "collapse",
        }
    )
