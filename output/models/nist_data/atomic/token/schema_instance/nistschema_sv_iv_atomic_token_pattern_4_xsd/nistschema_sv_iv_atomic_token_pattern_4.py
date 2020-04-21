from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicTokenPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-token-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\d{1,5}\s([A-Z][a-z]{1,20}\s){3}Street\s([A-Z][a-z]{1,20}\s){2},\s[A-Z]{2}\s13573"
        )
    )
