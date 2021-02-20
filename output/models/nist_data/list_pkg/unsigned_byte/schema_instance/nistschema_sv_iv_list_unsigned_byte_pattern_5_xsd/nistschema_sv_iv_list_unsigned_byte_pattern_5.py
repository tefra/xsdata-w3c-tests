from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedByte-pattern-5-NS"


@dataclass
class NistschemaSvIvListUnsignedBytePattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedByte-pattern-5"
        namespace = "NISTSchema-SV-IV-list-unsignedByte-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1} \d{2} \d{3} \d{1} \d{2} \d{3} \d{1}",
            "tokens": True,
        }
    )
