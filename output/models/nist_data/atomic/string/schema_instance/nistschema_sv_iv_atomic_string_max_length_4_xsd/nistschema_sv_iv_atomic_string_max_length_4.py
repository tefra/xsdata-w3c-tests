from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-maxLength-4-NS"


@dataclass
class NistschemaSvIvAtomicStringMaxLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-maxLength-4"
        namespace = "NISTSchema-SV-IV-atomic-string-maxLength-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_length=205.0
        )
    )
