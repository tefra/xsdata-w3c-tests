from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-pattern-5-NS"


@dataclass
class NistschemaSvIvListNmtokensPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-pattern-5"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\c{44} \c{22} \c{22} \c{56} \c{18} \c{15} \c{5} \c{38}"
        )
    )
