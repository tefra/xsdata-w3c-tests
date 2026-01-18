from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-maxLength-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNameMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-maxLength-1"
        namespace = "NISTSchema-SV-IV-atomic-Name-maxLength-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 1,
        },
    )
