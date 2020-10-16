from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateMaxExclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-date-maxExclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": "2016-09-05",
        }
    )
