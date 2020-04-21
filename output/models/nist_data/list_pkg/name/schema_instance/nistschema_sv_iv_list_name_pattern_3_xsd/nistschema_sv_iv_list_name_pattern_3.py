from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-Name-pattern-3-NS"


@dataclass
class NistschemaSvIvListNamePattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-Name-pattern-3"
        namespace = "NISTSchema-SV-IV-list-Name-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\i\c{24} \i\c{23} \i\c{57} \i\c{50} \i\c{52} \i\c{35} \i\c{28}"
        )
    )
