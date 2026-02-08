from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-length-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-length-5"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-length-5-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "length": 74,
            "format": "base16",
        },
    )
