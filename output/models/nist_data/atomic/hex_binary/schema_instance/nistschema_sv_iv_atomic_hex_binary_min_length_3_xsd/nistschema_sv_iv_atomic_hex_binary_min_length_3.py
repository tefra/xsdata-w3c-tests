from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-minLength-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-minLength-3"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-minLength-3-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "min_length": 2,
            "format": "base16",
        },
    )
