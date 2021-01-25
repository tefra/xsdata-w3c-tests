from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-pattern-4-NS"


@dataclass
class NistschemaSvIvListBase64BinaryPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-pattern-4"
        namespace = "NISTSchema-SV-IV-list-base64Binary-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"[a-zA-Z0-9+/]{48} [a-zA-Z0-9+/]{72} [a-zA-Z0-9+/]{52} [a-zA-Z0-9+/]{48} [a-zA-Z0-9+/]{12} [a-zA-Z0-9+/]{72} [a-zA-Z0-9+/]{68}",
            "tokens": True,
        }
    )
