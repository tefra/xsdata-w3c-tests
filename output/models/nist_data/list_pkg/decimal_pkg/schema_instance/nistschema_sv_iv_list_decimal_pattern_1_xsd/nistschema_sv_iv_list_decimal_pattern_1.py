from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-pattern-1-NS"


@dataclass
class NistschemaSvIvListDecimalPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-pattern-1"
        namespace = "NISTSchema-SV-IV-list-decimal-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1} \-\.\d{3} \-\d{3}\.\d{2} \d{6}\.\d{1} \-\d{2}\.\d{7} \d{7}\.\d{4} \-\d{4}\.\d{9} \-\d{4}\.\d{14}",
            "tokens": True,
        }
    )
