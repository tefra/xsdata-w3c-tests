from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-minLength-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBase64BinaryMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-minLength-5"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-minLength-5-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "min_length": 74,
            "format": "base64",
        },
    )
