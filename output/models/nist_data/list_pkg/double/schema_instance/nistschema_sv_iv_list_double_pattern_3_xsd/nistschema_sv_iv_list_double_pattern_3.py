from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-pattern-3-NS"


@dataclass
class NistschemaSvIvListDoublePattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-double-pattern-3"
        namespace = "NISTSchema-SV-IV-list-double-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"\d{1}E\-\d{3} \d{1}\.\d{3}E\-\d{2} \d{1}\.\d{6}E\-\d{1} \d{1}\.\d{9}E\d{1} \d{1}\.\d{12}E\d{2} \d{1}\.\d{16}E\d{3}",
            "tokens": True,
        }
    )
