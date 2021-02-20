from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedShort-pattern-2-NS"


@dataclass
class NistschemaSvIvListUnsignedShortPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedShort-pattern-2"
        namespace = "NISTSchema-SV-IV-list-unsignedShort-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1} \d{2} \d{3} \d{4} \d{5} \d{1} \d{2} \d{3}",
            "tokens": True,
        }
    )
