from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBooleanWhiteSpace2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-2"
        namespace = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-2-NS"

    value: bool = field(
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
