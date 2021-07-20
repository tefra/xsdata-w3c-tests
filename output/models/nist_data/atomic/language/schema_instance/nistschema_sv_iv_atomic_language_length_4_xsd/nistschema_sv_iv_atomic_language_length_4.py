from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-length-4-NS"


@dataclass
class NistschemaSvIvAtomicLanguageLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-length-4"
        namespace = "NISTSchema-SV-IV-atomic-language-length-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "length": 5,
        }
    )
