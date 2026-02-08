from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-maxLength-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNcnameMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-maxLength-1"
        namespace = "NISTSchema-SV-IV-atomic-NCName-maxLength-1-NS"

    value: str = field(
        default="",
        metadata={
            "max_length": 1,
        },
    )
