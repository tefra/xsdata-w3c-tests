from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive="1972-10-10T11:07:03"
        )
    )