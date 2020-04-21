from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive="2006-07-21T01:32:21"
        )
    )
