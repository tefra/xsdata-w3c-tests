from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-length-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBase64BinaryLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-length-4"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-length-4-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "length": 47,
            "format": "base64",
        },
    )
