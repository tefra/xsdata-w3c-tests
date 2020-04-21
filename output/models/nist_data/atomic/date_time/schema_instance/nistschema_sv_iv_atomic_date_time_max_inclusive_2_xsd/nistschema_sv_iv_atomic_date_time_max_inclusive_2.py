from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive="1982-05-22T18:01:37"
        )
    )
