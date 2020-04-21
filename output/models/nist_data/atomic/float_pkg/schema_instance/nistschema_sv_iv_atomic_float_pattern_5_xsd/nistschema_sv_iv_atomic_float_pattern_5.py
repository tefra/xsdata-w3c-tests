from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-float-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicFloatPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-float-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-float-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\d{1}\.\d{7}E\-\d{2}"
        )
    )
