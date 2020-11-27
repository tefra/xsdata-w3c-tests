from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-pattern-4-NS"


@dataclass
class NistschemaSvIvUnionDurationDecimalPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-pattern-4"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"P\d\d47Y\d3M1\dDT\d9H2\dM2\dS",
        }
    )
