from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-pattern-3-NS"


@dataclass
class NistschemaSvIvListBase64BinaryPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-pattern-3"
        namespace = "NISTSchema-SV-IV-list-base64Binary-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[a-zA-Z0-9+/]{12} [a-zA-Z0-9+/]{52} [a-zA-Z0-9+/]{28} [a-zA-Z0-9+/]{60} [a-zA-Z0-9+/]{20} [a-zA-Z0-9+/]{20} [a-zA-Z0-9+/]{48} [a-zA-Z0-9+/]{24} [a-zA-Z0-9+/]{72}",
            "tokens": True,
        }
    )
