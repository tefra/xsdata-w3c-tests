from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-length-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListBase64BinaryLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-length-2"
        namespace = "NISTSchema-SV-IV-list-base64Binary-length-2-NS"

    value: list[bytes] = field(
        default_factory=list,
        metadata={
            "length": 6,
            "tokens": True,
            "format": "base64",
        },
    )
