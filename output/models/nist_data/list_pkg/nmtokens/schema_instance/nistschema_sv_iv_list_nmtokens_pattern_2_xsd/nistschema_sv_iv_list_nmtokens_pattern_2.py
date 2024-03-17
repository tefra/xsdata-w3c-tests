from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-pattern-2-NS"


@dataclass
class NistschemaSvIvListNmtokensPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-pattern-2"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\c{64} \c{61} \c{8} \c{25} \c{14} \c{53} \c{12} \c{20}",
            "tokens": True,
        },
    )
