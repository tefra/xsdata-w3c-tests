from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-pattern-4-NS"


@dataclass
class NistschemaSvIvListGDayPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-pattern-4"
        namespace = "NISTSchema-SV-IV-list-gDay-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"---1\d ---2\d ---\d7 ---2\d ---\d6",
            "tokens": True,
        },
    )
