from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBase64BinaryMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-2"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-2-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "max_length": 45,
            "format": "base64",
        },
    )
