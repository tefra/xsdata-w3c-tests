from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedInt-pattern-1-NS"


@dataclass
class NistschemaSvIvListUnsignedIntPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedInt-pattern-1"
        namespace = "NISTSchema-SV-IV-list-unsignedInt-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"\d{1} \d{2} \d{3} \d{4} \d{5} \d{10}",
            "tokens": True,
        }
    )
