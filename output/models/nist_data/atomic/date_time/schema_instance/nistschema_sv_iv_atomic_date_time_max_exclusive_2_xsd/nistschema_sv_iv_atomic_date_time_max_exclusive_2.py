from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxExclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive="1980-05-22T13:12:09"
        )
    )
