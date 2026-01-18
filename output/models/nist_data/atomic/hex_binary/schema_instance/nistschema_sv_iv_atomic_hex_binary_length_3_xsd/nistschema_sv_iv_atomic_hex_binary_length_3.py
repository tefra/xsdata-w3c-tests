from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-length-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-length-3"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-length-3-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "required": True,
            "length": 41,
            "format": "base16",
        },
    )
