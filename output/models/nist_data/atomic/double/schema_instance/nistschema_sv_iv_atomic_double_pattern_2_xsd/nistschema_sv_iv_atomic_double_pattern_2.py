from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-double-pattern-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDoublePattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-double-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-double-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{1}\.\d{4}E\-\d{2}",
        },
    )
