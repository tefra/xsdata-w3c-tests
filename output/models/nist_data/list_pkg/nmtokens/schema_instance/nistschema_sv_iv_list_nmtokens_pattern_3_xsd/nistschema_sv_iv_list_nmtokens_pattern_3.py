from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-pattern-3-NS"


@dataclass
class NistschemaSvIvListNmtokensPattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-pattern-3"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-pattern-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\c{20} \c{48} \c{3} \c{54} \c{13} \c{29} \c{5}"
        )
    )
