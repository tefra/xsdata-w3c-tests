from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListNmtokensWhiteSpace1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-whiteSpace-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            white_space="collapse"
        )
    )
