from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-whiteSpace-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonNegativeIntegerWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-whiteSpace-1"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonNegativeInteger-whiteSpace-1-NS"
        )

    value: int = field(
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
