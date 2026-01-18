from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-minLength-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDecimalMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-minLength-1"
        namespace = "NISTSchema-SV-IV-list-decimal-minLength-1-NS"

    value: list[Decimal] = field(
        default_factory=list,
        metadata={
            "min_length": 5,
            "tokens": True,
        },
    )
