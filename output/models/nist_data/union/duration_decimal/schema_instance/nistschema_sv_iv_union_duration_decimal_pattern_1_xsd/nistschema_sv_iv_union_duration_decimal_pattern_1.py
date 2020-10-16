from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-pattern-1-NS"


@dataclass
class NistschemaSvIvUnionDurationDecimalPattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-pattern-1"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-pattern-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\-\.\d{5}",
        }
    )
