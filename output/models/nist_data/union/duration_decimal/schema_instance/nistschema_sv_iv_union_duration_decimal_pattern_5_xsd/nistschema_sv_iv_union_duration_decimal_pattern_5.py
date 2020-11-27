from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-pattern-5-NS"


@dataclass
class NistschemaSvIvUnionDurationDecimalPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-pattern-5"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\-\d{1}",
        }
    )
