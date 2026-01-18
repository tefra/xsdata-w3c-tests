from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-minLength-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNameMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-minLength-3"
        namespace = "NISTSchema-SV-IV-atomic-Name-minLength-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 28,
        },
    )
