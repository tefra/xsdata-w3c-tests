from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedShort-pattern-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListUnsignedShortPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedShort-pattern-4"
        namespace = "NISTSchema-SV-IV-list-unsignedShort-pattern-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1} \d{2} \d{3} \d{4} \d{5} \d{1}",
            "tokens": True,
        },
    )
