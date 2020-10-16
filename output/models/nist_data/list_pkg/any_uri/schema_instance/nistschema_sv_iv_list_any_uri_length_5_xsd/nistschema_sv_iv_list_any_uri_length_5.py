from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-anyURI-length-5-NS"


@dataclass
class NistschemaSvIvListAnyUriLength5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-anyURI-length-5"
        namespace = "NISTSchema-SV-IV-list-anyURI-length-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 10,
            "tokens": True,
        }
    )
