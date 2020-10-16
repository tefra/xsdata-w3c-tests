from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDurationMaxExclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxExclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": "P1990Y06M11DT15H00M05S",
        }
    )
