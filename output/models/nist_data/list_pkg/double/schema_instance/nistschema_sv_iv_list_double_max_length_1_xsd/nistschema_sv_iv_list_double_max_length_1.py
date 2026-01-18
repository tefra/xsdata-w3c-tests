from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-maxLength-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDoubleMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-double-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-double-maxLength-1-NS"

    value: list[float] = field(
        default_factory=list,
        metadata={
            "max_length": 5,
            "tokens": True,
        },
    )
