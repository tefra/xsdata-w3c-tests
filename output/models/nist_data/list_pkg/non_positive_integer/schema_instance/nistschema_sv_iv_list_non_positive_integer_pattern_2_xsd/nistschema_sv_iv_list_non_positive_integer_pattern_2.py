from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-nonPositiveInteger-pattern-2-NS"


@dataclass
class NistschemaSvIvListNonPositiveIntegerPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-nonPositiveInteger-pattern-2"
        namespace = "NISTSchema-SV-IV-list-nonPositiveInteger-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"\-\d{1} \-\d{5} \-\d{9} \-\d{13} \-\d{18}",
            "tokens": True,
        }
    )
