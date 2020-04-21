from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxInclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive="2003-03-09T02:00:23"
        )
    )
