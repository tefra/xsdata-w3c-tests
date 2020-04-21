from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinExclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive="1974-04-26T23:23:51"
        )
    )
