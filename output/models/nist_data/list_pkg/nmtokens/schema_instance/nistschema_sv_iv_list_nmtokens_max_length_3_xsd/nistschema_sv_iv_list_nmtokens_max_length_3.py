from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-maxLength-3-NS"


@dataclass
class NistschemaSvIvListNmtokensMaxLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-maxLength-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_length=7
        )
    )
