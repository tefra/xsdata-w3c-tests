from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKEN-pattern-3-NS"


@dataclass
class NistschemaSvIvListNmtokenPattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKEN-pattern-3"
        namespace = "NISTSchema-SV-IV-list-NMTOKEN-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"\c{1} \c{36} \c{63} \c{7} \c{26} \c{11} \c{55} \c{29}",
            tokens=True
        )
    )
