from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-length-3-NS"


@dataclass
class NistschemaSvIvListNmtokensLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-length-3"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-length-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 7,
            "tokens": True,
        }
    )
