from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-maxLength-2-NS"


@dataclass
class NistschemaSvIvListNmtokensMaxLength2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-maxLength-2"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-maxLength-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_length=6
        )
    )
