from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinExclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive="2001-09-04T00:13:18"
        )
    )
