from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-maxLength-4-NS"


@dataclass
class NistschemaSvIvAtomicNcnameMaxLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-maxLength-4"
        namespace = "NISTSchema-SV-IV-atomic-NCName-maxLength-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_length": 37,
        }
    )
