from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-length-3-NS"


@dataclass
class NistschemaSvIvListNmtokensLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-length-3"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-length-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            length=7
        )
    )