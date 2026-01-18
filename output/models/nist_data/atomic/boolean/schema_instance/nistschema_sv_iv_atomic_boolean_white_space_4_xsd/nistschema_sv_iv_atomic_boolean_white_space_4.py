from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBooleanWhiteSpace4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-4"
        namespace = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-4-NS"

    value: bool = field(
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
