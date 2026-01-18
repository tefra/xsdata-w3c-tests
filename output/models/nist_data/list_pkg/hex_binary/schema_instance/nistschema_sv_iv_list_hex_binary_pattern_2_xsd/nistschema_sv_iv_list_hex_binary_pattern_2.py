from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-pattern-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListHexBinaryPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-pattern-2"
        namespace = "NISTSchema-SV-IV-list-hexBinary-pattern-2-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[0-9A-F]{2} [0-9A-F]{2} [0-9A-F]{8} [0-9A-F]{62} [0-9A-F]{40} [0-9A-F]{34} [0-9A-F]{72} [0-9A-F]{10} [0-9A-F]{34} [0-9A-F]{12}",
            "tokens": True,
        },
    )
