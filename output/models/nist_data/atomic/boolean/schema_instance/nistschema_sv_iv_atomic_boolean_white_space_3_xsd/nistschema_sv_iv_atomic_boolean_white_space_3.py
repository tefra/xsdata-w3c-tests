from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBooleanWhiteSpace3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-3"
        namespace = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-3-NS"

    value: bool = field(
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
