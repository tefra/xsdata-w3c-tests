from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-positiveInteger-maxLength-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListPositiveIntegerMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-positiveInteger-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-positiveInteger-maxLength-5-NS"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "max_length": 10,
            "tokens": True,
        },
    )
