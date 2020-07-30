from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-minLength-4-NS"


@dataclass
class NistschemaSvIvListNmtokensMinLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-minLength-4"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-minLength-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_length=8
        )
    )
