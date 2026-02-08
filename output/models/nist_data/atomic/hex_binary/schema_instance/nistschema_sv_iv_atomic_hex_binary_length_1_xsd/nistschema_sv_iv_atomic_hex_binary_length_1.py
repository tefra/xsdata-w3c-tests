from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-length-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-length-1"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-length-1-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "length": 1,
            "format": "base16",
        },
    )
