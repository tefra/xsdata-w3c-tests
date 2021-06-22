from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-pattern-5-NS"


@dataclass
class NistschemaSvIvUnionShortGYearPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-pattern-5"
        namespace = "NISTSchema-SV-IV-union-short-gYear-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"\d{5}",
        }
    )
