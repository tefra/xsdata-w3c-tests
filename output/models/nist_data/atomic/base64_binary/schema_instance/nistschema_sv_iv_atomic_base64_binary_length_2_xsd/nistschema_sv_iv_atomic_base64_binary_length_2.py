from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-length-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBase64BinaryLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-length-2"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-length-2-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "length": 1,
            "format": "base64",
        },
    )
