from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-pattern-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBase64BinaryPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-pattern-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[a-zA-Z0-9+/]{24}",
        },
    )
