from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBooleanWhiteSpace5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-5"
        namespace = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-5-NS"

    value: bool = field(
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
