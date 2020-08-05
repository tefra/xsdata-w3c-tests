from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-minLength-1-NS"


@dataclass
class NistschemaSvIvListNmtokensMinLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-minLength-1"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-minLength-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            min_length=5,
            tokens=True
        )
    )
