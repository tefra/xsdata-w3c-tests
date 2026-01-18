from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-length-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListHexBinaryLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-length-4"
        namespace = "NISTSchema-SV-IV-list-hexBinary-length-4-NS"

    value: list[bytes] = field(
        default_factory=list,
        metadata={
            "length": 8,
            "tokens": True,
            "format": "base16",
        },
    )
