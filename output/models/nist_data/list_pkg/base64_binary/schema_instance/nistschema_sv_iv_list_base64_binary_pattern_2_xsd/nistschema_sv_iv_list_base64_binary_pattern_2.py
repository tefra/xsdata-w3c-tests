from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-pattern-2-NS"


@dataclass
class NistschemaSvIvListBase64BinaryPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-pattern-2"
        namespace = "NISTSchema-SV-IV-list-base64Binary-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"[a-zA-Z0-9+/]{32} [a-zA-Z0-9+/]{60} [a-zA-Z0-9+/]{60} [a-zA-Z0-9+/]{32} [a-zA-Z0-9+/]{48} [a-zA-Z0-9+/]{36} [a-zA-Z0-9+/]{48}"
        )
    )