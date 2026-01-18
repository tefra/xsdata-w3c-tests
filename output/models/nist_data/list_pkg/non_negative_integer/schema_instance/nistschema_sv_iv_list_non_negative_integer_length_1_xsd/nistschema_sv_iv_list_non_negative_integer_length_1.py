from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-nonNegativeInteger-length-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListNonNegativeIntegerLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-nonNegativeInteger-length-1"
        namespace = "NISTSchema-SV-IV-list-nonNegativeInteger-length-1-NS"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "length": 5,
            "tokens": True,
        },
    )
