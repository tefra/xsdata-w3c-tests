from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-length-2-NS"


@dataclass
class NistschemaSvIvListNmtokensLength2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-length-2"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-length-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            length=6
        )
    )
