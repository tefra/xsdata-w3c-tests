from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-4"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-4-NS"

    value: bytes = field(
        default=b"",
        metadata={
            "required": True,
            "max_length": 6,
            "format": "base16",
        },
    )
