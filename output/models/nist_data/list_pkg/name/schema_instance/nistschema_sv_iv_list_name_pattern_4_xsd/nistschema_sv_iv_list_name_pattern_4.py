from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-Name-pattern-4-NS"


@dataclass
class NistschemaSvIvListNamePattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-Name-pattern-4"
        namespace = "NISTSchema-SV-IV-list-Name-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\i\c{19} \i\c{63} \i\c{18} \i\c{40} \i\c{12} \i\c{58} \i\c{47} \i\c{54} \i\c{15}",
            "tokens": True,
        }
    )
