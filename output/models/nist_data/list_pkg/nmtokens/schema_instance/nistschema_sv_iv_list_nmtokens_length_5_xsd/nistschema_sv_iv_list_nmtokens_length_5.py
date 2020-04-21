from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-length-5-NS"


@dataclass
class NistschemaSvIvListNmtokensLength5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-length-5"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-length-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            length=10
        )
    )
