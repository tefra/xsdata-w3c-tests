from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDurationMinExclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-duration-minExclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive="P2015Y06M12DT06H42M35S"
        )
    )