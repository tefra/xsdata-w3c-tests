from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-int-pattern-3-NS"


@dataclass
class NistschemaSvIvListIntPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-int-pattern-3"
        namespace = "NISTSchema-SV-IV-list-int-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"\-\d{10} \-\d{5} \-\d{3} \-\d{1} \d{2} \d{4} \d{10}",
            "tokens": True,
        }
    )
