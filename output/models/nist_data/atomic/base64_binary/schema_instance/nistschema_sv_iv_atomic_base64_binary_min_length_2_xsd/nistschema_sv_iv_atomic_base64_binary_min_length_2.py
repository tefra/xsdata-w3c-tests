from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-minLength-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBase64BinaryMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-minLength-2"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-minLength-2-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "required": True,
            "min_length": 27,
            "format": "base64",
        },
    )
