from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-length-4-NS"


@dataclass
class NistschemaSvIvAtomicNcnameLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-length-4"
        namespace = "NISTSchema-SV-IV-atomic-NCName-length-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "length": 61,
        }
    )
