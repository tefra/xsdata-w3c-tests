from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-float-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicFloatPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-float-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-float-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"\d{1}\.\d{3}E\d{2}",
        }
    )
