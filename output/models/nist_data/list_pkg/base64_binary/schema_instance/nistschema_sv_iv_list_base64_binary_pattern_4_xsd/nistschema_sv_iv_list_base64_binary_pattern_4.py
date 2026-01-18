from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-pattern-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListBase64BinaryPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-pattern-4"
        namespace = "NISTSchema-SV-IV-list-base64Binary-pattern-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[a-zA-Z0-9+/]{48} [a-zA-Z0-9+/]{72} [a-zA-Z0-9+/]{52} [a-zA-Z0-9+/]{48} [a-zA-Z0-9+/]{12} [a-zA-Z0-9+/]{72} [a-zA-Z0-9+/]{68}",
            "tokens": True,
        },
    )
