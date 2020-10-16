from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDurationMaxExclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxExclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": "P1983Y12M12DT16H37M58S",
        }
    )
