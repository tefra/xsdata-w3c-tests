from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicDateTimePattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\d\d77-0\d-0\dT1\d:\d5:\d5"
        )
    )
