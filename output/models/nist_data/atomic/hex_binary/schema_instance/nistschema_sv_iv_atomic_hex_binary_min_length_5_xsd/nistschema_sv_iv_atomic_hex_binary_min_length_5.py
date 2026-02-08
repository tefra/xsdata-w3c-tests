from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-minLength-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-minLength-5"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-minLength-5-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "min_length": 74,
            "format": "base16",
        },
    )
