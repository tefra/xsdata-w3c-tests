from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-pattern-4-NS"


@dataclass
class NistschemaSvIvListNmtokensPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-pattern-4"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\c{29} \c{7} \c{23} \c{2} \c{63} \c{24} \c{34} \c{59}"
        )
    )
