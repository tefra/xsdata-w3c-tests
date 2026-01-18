from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-length-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicBase64BinaryLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-length-5"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-length-5-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "required": True,
            "length": 74,
            "format": "base64",
        },
    )
