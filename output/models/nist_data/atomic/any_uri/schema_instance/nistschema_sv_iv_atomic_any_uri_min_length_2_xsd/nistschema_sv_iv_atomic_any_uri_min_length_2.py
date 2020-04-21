from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-minLength-2-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriMinLength2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-minLength-2"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-minLength-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_length=41.0
        )
    )
