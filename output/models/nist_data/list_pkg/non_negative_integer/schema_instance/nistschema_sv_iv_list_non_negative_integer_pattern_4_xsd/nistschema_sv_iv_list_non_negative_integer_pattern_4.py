from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-nonNegativeInteger-pattern-4-NS"


@dataclass
class NistschemaSvIvListNonNegativeIntegerPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-nonNegativeInteger-pattern-4"
        namespace = "NISTSchema-SV-IV-list-nonNegativeInteger-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1} \d{3} \d{5} \d{7} \d{9} \d{11} \d{18}",
            "tokens": True,
        },
    )
