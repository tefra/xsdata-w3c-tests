from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-minLength-2-NS"


@dataclass
class NistschemaSvIvAtomicNcnameMinLength2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-minLength-2"
        namespace = "NISTSchema-SV-IV-atomic-NCName-minLength-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_length=47.0
        )
    )