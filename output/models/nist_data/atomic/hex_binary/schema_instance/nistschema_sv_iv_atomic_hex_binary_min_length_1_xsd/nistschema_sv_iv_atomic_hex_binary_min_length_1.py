from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-minLength-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-minLength-1"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-minLength-1-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "required": True,
            "min_length": 1,
            "format": "base16",
        },
    )
