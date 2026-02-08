from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-pattern-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNamePattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-Name-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\i\c{32}",
        },
    )
