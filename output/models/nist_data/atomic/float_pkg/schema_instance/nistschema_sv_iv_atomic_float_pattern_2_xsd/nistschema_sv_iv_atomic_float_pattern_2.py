from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-float-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicFloatPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-float-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-float-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"\d{2}E\-\d{1}",
        }
    )
