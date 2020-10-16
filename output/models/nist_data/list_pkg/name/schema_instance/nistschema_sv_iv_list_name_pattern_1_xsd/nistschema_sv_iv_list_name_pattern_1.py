from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-Name-pattern-1-NS"


@dataclass
class NistschemaSvIvListNamePattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-Name-pattern-1"
        namespace = "NISTSchema-SV-IV-list-Name-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"\i\c{48} \i\c{47} \i\c{13} \i\c{4} \i\c{46} \i\c{37}",
            "tokens": True,
        }
    )
