from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-pattern-3-NS"


@dataclass
class NistschemaSvIvListGDayPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-pattern-3"
        namespace = "NISTSchema-SV-IV-list-gDay-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"---\d5 ---0\d ---\d1 ---0\d ---2\d ---1\d ---\d1",
            "tokens": True,
        }
    )
