from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive="1972-09-29T19:51:19"
        )
    )
