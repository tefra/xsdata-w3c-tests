from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-pattern-1-NS"


@dataclass
class NistschemaSvIvListNmtokensPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-pattern-1"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"\c{16} \c{9} \c{44} \c{34} \c{46} \c{6}",
            "tokens": True,
        },
    )
