from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-whiteSpace-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicStringWhiteSpace2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-whiteSpace-2"
        namespace = "NISTSchema-SV-IV-atomic-string-whiteSpace-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "collapse",
        },
    )
