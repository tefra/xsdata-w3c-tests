from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-double-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicDoublePattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-double-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-double-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"\d{1}\.\d{4}E\-\d{2}",
        }
    )
