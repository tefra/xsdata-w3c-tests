from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-minLength-1-NS"


@dataclass
class NistschemaSvIvAtomicLanguageMinLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-minLength-1"
        namespace = "NISTSchema-SV-IV-atomic-language-minLength-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_length=2.0
        )
    )