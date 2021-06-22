from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-pattern-1-NS"


@dataclass
class NistschemaSvIvUnionShortGYearPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-pattern-1"
        namespace = "NISTSchema-SV-IV-union-short-gYear-pattern-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"\d\d70",
        }
    )
