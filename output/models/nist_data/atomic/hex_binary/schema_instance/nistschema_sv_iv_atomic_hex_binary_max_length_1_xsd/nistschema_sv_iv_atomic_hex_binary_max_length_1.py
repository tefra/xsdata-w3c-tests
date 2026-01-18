from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-1"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-1-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "required": True,
            "max_length": 1,
            "format": "base16",
        },
    )
