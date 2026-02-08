from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-minLength-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-minLength-4"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-minLength-4-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "min_length": 48,
            "format": "base16",
        },
    )
