from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-minLength-3-NS"


@dataclass
class NistschemaSvIvAtomicStringMinLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-minLength-3"
        namespace = "NISTSchema-SV-IV-atomic-string-minLength-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_length=90
        )
    )
