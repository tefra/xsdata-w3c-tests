from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-length-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-length-4"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-length-4-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "required": True,
            "length": 68,
            "format": "base16",
        },
    )
