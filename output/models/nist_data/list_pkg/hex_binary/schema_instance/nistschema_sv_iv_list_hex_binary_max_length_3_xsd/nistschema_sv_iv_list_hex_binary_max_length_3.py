from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-maxLength-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListHexBinaryMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-hexBinary-maxLength-3-NS"

    value: list[bytes] = field(
        default_factory=list,
        metadata={
            "max_length": 7,
            "tokens": True,
            "format": "base16",
        },
    )
