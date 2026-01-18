from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-double-pattern-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDoublePattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-double-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-double-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{1}\.\d{8}E\-\d{1}",
        },
    )
