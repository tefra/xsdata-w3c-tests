from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-integer-pattern-2-NS"


@dataclass
class NistschemaSvIvListIntegerPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-integer-pattern-2"
        namespace = "NISTSchema-SV-IV-list-integer-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\-\d{18} \-\d{10} \-\d{4} \d{1} \d{7} \d{18}",
            "tokens": True,
        },
    )
