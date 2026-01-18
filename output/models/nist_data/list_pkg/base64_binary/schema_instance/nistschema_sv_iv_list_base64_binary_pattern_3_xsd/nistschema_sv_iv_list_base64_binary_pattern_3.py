from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-pattern-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListBase64BinaryPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-pattern-3"
        namespace = "NISTSchema-SV-IV-list-base64Binary-pattern-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[a-zA-Z0-9+/]{12} [a-zA-Z0-9+/]{52} [a-zA-Z0-9+/]{28} [a-zA-Z0-9+/]{60} [a-zA-Z0-9+/]{20} [a-zA-Z0-9+/]{20} [a-zA-Z0-9+/]{48} [a-zA-Z0-9+/]{24} [a-zA-Z0-9+/]{72}",
            "tokens": True,
        },
    )
