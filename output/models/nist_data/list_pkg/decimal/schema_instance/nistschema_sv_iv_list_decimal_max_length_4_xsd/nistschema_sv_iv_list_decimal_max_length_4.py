from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-maxLength-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDecimalMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-maxLength-4"
        namespace = "NISTSchema-SV-IV-list-decimal-maxLength-4-NS"

    value: list[Decimal] = field(
        default_factory=list,
        metadata={
            "max_length": 8,
            "tokens": True,
        },
    )
