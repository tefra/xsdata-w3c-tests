from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-minLength-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListHexBinaryMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-minLength-4"
        namespace = "NISTSchema-SV-IV-list-hexBinary-minLength-4-NS"

    value: list[bytes] = field(
        default_factory=list,
        metadata={
            "min_length": 8,
            "tokens": True,
            "format": "base16",
        },
    )
