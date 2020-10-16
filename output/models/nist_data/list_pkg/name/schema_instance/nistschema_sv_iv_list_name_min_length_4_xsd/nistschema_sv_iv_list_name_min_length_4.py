from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-Name-minLength-4-NS"


@dataclass
class NistschemaSvIvListNameMinLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-Name-minLength-4"
        namespace = "NISTSchema-SV-IV-list-Name-minLength-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 8,
            "tokens": True,
        }
    )
