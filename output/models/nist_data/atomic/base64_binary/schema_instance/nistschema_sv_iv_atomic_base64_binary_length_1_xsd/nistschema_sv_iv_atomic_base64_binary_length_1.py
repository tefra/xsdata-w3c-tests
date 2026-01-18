from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-length-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBase64BinaryLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-length-1"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-length-1-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "required": True,
            "length": 1,
            "format": "base64",
        },
    )
