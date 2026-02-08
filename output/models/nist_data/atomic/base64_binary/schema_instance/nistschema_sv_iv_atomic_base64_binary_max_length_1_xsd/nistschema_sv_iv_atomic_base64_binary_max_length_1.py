from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBase64BinaryMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-1"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-1-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "max_length": 1,
            "format": "base64",
        },
    )
