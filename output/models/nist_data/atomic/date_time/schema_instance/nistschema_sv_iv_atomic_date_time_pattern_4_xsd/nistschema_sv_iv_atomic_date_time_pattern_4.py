from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicDateTimePattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\d\d89-\d2-\d0T1\d:2\d:1\d"
        )
    )