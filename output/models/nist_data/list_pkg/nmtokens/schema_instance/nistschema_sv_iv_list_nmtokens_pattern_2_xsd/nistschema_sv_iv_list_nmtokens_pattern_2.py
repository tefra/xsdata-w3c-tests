from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-pattern-2-NS"


@dataclass
class NistschemaSvIvListNmtokensPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-pattern-2"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\c{64} \c{61} \c{8} \c{25} \c{14} \c{53} \c{12} \c{20}"
        )
    )