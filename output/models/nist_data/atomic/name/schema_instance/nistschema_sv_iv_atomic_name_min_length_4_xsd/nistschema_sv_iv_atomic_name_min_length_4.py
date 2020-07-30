from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-minLength-4-NS"


@dataclass
class NistschemaSvIvAtomicNameMinLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-minLength-4"
        namespace = "NISTSchema-SV-IV-atomic-Name-minLength-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_length=54
        )
    )
