from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKEN-pattern-1-NS"


@dataclass
class NistschemaSvIvListNmtokenPattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKEN-pattern-1"
        namespace = "NISTSchema-SV-IV-list-NMTOKEN-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\c{40} \c{21} \c{50} \c{36} \c{35} \c{42} \c{54} \c{48}"
        )
    )
