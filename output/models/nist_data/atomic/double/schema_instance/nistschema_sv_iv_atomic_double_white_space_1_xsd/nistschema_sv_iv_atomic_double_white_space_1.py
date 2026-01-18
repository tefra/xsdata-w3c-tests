from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-double-whiteSpace-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDoubleWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-double-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-double-whiteSpace-1-NS"

    value: float = field(
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
