from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-maxLength-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNcnameMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-maxLength-3"
        namespace = "NISTSchema-SV-IV-atomic-NCName-maxLength-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 12,
        },
    )
