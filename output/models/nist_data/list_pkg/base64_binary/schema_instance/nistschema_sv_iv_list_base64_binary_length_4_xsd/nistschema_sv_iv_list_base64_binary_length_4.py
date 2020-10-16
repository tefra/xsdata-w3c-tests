from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-length-4-NS"


@dataclass
class NistschemaSvIvListBase64BinaryLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-length-4"
        namespace = "NISTSchema-SV-IV-list-base64Binary-length-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 8,
            "tokens": True,
        }
    )
