from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-whiteSpace-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicStringWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-string-whiteSpace-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "preserve",
        },
    )
