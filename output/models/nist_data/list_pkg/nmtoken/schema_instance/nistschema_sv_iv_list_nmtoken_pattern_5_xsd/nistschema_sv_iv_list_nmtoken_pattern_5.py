from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKEN-pattern-5-NS"


@dataclass
class NistschemaSvIvListNmtokenPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKEN-pattern-5"
        namespace = "NISTSchema-SV-IV-list-NMTOKEN-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\c{45} \c{5} \c{56} \c{45} \c{33} \c{37} \c{45} \c{40}"
        )
    )
