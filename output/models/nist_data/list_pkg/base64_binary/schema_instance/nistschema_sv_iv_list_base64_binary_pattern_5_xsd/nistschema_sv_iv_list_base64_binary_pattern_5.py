from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-pattern-5-NS"


@dataclass
class NistschemaSvIvListBase64BinaryPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-pattern-5"
        namespace = "NISTSchema-SV-IV-list-base64Binary-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"[a-zA-Z0-9+/]{36} [a-zA-Z0-9+/]{52} [a-zA-Z0-9+/]{40} [a-zA-Z0-9+/]{56} [a-zA-Z0-9+/]{56} [a-zA-Z0-9+/]{40} [a-zA-Z0-9+/]{56}"
        )
    )