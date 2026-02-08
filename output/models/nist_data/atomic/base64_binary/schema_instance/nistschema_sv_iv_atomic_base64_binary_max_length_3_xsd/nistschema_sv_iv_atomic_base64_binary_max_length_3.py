from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBase64BinaryMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-3"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-3-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "max_length": 54,
            "format": "base64",
        },
    )
