from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKEN-pattern-2-NS"


@dataclass
class NistschemaSvIvListNmtokenPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKEN-pattern-2"
        namespace = "NISTSchema-SV-IV-list-NMTOKEN-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"\c{20} \c{60} \c{47} \c{22} \c{42} \c{14}",
            tokens=True
        )
    )
