from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBase64BinaryMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-4"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-4-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "max_length": 61,
            "format": "base64",
        },
    )
