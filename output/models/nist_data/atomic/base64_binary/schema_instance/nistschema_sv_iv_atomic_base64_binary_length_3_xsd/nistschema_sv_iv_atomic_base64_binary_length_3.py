from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-length-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBase64BinaryLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-length-3"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-length-3-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "length": 31,
            "format": "base64",
        },
    )
