from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-negativeInteger-minLength-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListNegativeIntegerMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-negativeInteger-minLength-1"
        namespace = "NISTSchema-SV-IV-list-negativeInteger-minLength-1-NS"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "min_length": 5,
            "tokens": True,
        },
    )
