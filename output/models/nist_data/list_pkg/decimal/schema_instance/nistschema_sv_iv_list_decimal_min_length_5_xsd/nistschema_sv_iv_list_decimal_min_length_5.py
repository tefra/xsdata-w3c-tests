from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-minLength-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDecimalMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-minLength-5"
        namespace = "NISTSchema-SV-IV-list-decimal-minLength-5-NS"

    value: list[Decimal] = field(
        default_factory=list,
        metadata={
            "min_length": 10,
            "tokens": True,
        },
    )
