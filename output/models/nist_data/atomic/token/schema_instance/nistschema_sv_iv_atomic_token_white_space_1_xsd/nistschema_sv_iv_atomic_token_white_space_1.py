from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-whiteSpace-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTokenWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-token-whiteSpace-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "collapse",
        },
    )
