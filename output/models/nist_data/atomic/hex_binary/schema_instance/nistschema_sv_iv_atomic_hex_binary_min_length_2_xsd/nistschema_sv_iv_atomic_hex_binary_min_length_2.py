from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-minLength-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-minLength-2"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-minLength-2-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "required": True,
            "min_length": 28,
            "format": "base16",
        },
    )
