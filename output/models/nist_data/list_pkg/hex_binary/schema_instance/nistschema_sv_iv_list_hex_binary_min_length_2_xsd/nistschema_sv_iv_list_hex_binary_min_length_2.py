from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-minLength-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListHexBinaryMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-minLength-2"
        namespace = "NISTSchema-SV-IV-list-hexBinary-minLength-2-NS"

    value: list[bytes] = field(
        default_factory=list,
        metadata={
            "min_length": 6,
            "tokens": True,
            "format": "base16",
        },
    )
