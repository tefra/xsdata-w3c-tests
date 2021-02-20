from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-pattern-5-NS"


@dataclass
class NistschemaSvIvListHexBinaryPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-pattern-5"
        namespace = "NISTSchema-SV-IV-list-hexBinary-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[0-9A-F]{30} [0-9A-F]{2} [0-9A-F]{18} [0-9A-F]{32} [0-9A-F]{52} [0-9A-F]{30} [0-9A-F]{30}",
            "tokens": True,
        }
    )
