from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedInt-pattern-4-NS"


@dataclass
class NistschemaSvIvListUnsignedIntPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedInt-pattern-4"
        namespace = "NISTSchema-SV-IV-list-unsignedInt-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1} \d{2} \d{3} \d{4} \d{5} \d{6} \d{7} \d{10}",
            "tokens": True,
        },
    )
