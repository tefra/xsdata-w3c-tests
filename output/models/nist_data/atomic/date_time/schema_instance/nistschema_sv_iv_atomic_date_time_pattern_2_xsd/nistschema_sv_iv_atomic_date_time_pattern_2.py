from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicDateTimePattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\d\d55-0\d-\d8T\d6:1\d:0\d"
        )
    )
