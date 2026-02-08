from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-3"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-3-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "max_length": 7,
            "format": "base16",
        },
    )
