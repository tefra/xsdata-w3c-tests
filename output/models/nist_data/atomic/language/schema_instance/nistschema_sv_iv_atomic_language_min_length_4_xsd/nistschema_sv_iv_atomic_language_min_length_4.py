from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-minLength-4-NS"


@dataclass
class NistschemaSvIvAtomicLanguageMinLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-minLength-4"
        namespace = "NISTSchema-SV-IV-atomic-language-minLength-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_length=4.0
        )
    )