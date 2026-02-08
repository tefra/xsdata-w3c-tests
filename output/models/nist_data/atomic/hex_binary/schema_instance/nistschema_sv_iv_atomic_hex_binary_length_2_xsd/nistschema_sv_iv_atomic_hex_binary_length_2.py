from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-length-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-length-2"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-length-2-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "length": 16,
            "format": "base16",
        },
    )
