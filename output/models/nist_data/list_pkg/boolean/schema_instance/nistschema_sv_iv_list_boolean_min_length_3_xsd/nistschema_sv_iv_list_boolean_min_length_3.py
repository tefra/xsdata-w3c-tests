from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-minLength-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListBooleanMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-minLength-3"
        namespace = "NISTSchema-SV-IV-list-boolean-minLength-3-NS"

    value: list[bool] = field(
        default_factory=list,
        metadata={
            "min_length": 7,
            "tokens": True,
        },
    )
