from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-pattern-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListHexBinaryPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-pattern-5"
        namespace = "NISTSchema-SV-IV-list-hexBinary-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[0-9A-F]{30} [0-9A-F]{2} [0-9A-F]{18} [0-9A-F]{32} [0-9A-F]{52} [0-9A-F]{30} [0-9A-F]{30}",
            "tokens": True,
        },
    )
